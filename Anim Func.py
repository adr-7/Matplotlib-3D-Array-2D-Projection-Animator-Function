import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import PowerNorm

def StackRangeAnimation(dataset,x,y,thickness,log=False,mean=False,anim_mode="linear",save=False,show=True,FName="NameYourFile",TName="SetYourTitle"):
    #  GLOBAL STYLE
    plt.style.use(['ggplot', 'dark_background'])
    plt.rcParams['axes.grid'] = False
    
    #  CREATING PRIMARY SUBPLOT
    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.set_xlabel('Cells')
    
    #  PRE-CALCULATING DESIRED DATASET TRANSFORMATIONS
    if log==True and mean==True:
        processed = np.log10(1 + (dataset - np.mean(dataset))/(np.mean(dataset)))
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position("right")
        ax.set_ylabel('Orders of Magnitude Relative to Mean', rotation=-90, labelpad=70)
    elif log==True and mean==False:
        processed = np.log10(dataset)
    elif log==False and mean==True:
        processed = processed = (1 + (dataset - np.mean(dataset))/(np.mean(dataset)))
    elif log==False and mean==False:
        processed = dataset

    #  VISUAL SETTINGS AND DEFINING A FRAME
    norm = PowerNorm(gamma=1.5) # sets the norm type. alternates: LogNorm()
    normval = f"{norm.__class__.__name__}"
    cmap = "inferno"
    img = ax.imshow(np.sum(processed[:,:,x:(x+thickness)], axis=2), cmap=cmap, norm=norm)

    #  ADDING COLORBAR
    divider = make_axes_locatable(ax)
    cbar_ax = divider.append_axes("right", size="5%", pad = 0.05)
    cbar = fig.colorbar(img, cax=cbar_ax, orientation='vertical')

    #  ASSIGNING FRAMES VARIALBE, LINEAR AND REFLECT
    linear = list(range(x,y-thickness))
    reflect = (list(range(x,y-thickness)) + list(range(y-1-thickness,x,-1)))
    if anim_mode == "reflect":
        frames = reflect
    elif anim_mode == "linear":
        frames = linear

    #  FRAME UPDATING FUNCTION
    def update(i):
        img.set_array(np.sum(processed[:,:,i:(i+thickness)], axis=2))
        ax.set_title(f"{TName} on Slice {i}\nSum Width of {thickness}, Normalization Mode: {normval}, Colormap: {cmap}\nLog={log}, Mean={mean}")
        return [img]
    
    #  ANIMATION FUNCTION
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=(1000/24), blit=False , repeat=True) # please dont try blit=True its a mess

    #  SAVE/SHOW 
    if save==True:
        mpl.rcParams['animation.ffmpeg_args'] = ["-vcodec", "libx264", "-crf", "16", "-preset", "slow"]
        ani.save(f"{FName}.mov", writer='ffmpeg',fps=24, dpi=200)
    if show==True:
        plt.show()