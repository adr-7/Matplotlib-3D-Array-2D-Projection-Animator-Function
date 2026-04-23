# Matplotlib-3D-Array-2D-Projection-Animator-Function
Takes a 3D array and projects it onto a 2D slice of desired thickness, and then iterates that slice through the array to form an animation.


https://github.com/user-attachments/assets/b5c00256-5d06-464a-956a-2419227c1281


The first three function variables are required. StackRangeAnimation(dataset,x,y,thickness) where dataset is the desired 3D array, x is the start range, y is the end, and thickness describes the width of the plane that is iterated through the array.
- Example: StackRangeAnimation(density,1,512,20)
    
    
The optional (but reccomended) variables are as follows:
    
log - Takes the log of the array. Defaults to False.
- Example: log=False
    
mean - Transforms the array to only contain values above the mean value. Defaults to False.
- Example: mean=True

If log and mean are both True, the function outputs density color values as orders of magnitudes above the mean value. This is highly reccomended in order to assign clearer meaning to colorbar number values.
    
anim_mode - Changes the mode of animation between two options: linear and reflect. Linear passes though the function once, while reflect plays through, and then in reverse back to the starting start value (ideal for gifs). Defaults to "linear".
- Example: anim_mode="reflect"

save - Toggles whether the animation is saved to the working directory. Defaults to False.
- Example: save=True

show - Toggles whether the animation is displayed. Defaults to True.
- Example: show=True

FName - Sets the saved file name. Defaults to "NameYourFile".
- Example: Fname="Density_DM"

TName - Sets the plot title. Defaults to "SetYourTitle".
- Example: TName="Density of DM"
