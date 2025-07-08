# conways game of life 07/07/25 to 08/07/2025
import numpy as np
import matplotlib.pyplot as plt

n = int(input("enter the size grid you would like: "))

print("creating grid...")
print("you can click cells to plot")

grid = np.random.randint(0, 2, size=(n, n))
print(grid)

def count_neighbours(i,j,size):
    global grid
    count = 0
    if i < size and grid[i+1,j]==1: # adjacent below
        count+=1
    if j < size and grid[i,j+1]==1: # adjacent right
        count+=1
    if j < size and i < size and grid[i+1,j+1]==1: # adjacent right below
        count+=1
    if i > 0 and grid[i-1,j]==1: # adjacent above
        count+=1
    if j > 0 and grid[i,j-1]==1: # adjacent left
        count+=1
    if j > 0 and i > 0 and grid[i-1,j-1]==1: # adjacent above left
        count+=1
    if j < size and i > 0 and grid[i-1,j+1]==1: # adjacent above right
        count+=1
    if j > 0 and i < size and grid[i+1,j-1]==1: # adjacent below left
        count+=1 
    return(count) 

def update_grid():
    global grid
    size = len(grid)
    new_grid=np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            neighbours = count_neighbours(i,j,size-1)
            if grid[i,j] == 1:
                if neighbours == 2 or neighbours == 3:
                    new_grid[i,j] = 1 # survivial
                else:
                    new_grid[i,j] = 0 # under or over population
            elif grid[i,j] == 0 and neighbours == 3:
                new_grid[i,j] = 1 # birth
    return(new_grid)

def on_click(event): # allow interaction with grid
    global grid
    if event.inaxes != ax:
        return
    i, j = int(event.ydata), int(event.xdata)
    if 0 <= i < n and 0 <= j < n:
        grid[i, j] = 1
        img.set_data(1 - grid)
        fig.canvas.draw_idle()

plt.ion() # set up plotting
fig, ax = plt.subplots()
img = ax.imshow(1 - grid, cmap='gray', vmin=0, vmax=1)
ax.set_xticks(np.arange(n))
ax.set_yticks(np.arange(n))
ax.set_xticks(np.arange(-.5, n, 1), minor=True)
ax.set_yticks(np.arange(-.5, n, 1), minor=True)
ax.grid(which='minor', color='black', linewidth=0.5)
ax.set_aspect('equal')

# take input
fig.canvas.mpl_connect('button_press_event', on_click)

while True:
    plt.pause(0.5)
    if input("Type 'stop' to end: ").strip().lower() == 'stop':
        break
    grid = update_grid()
    fig.canvas.draw_idle()
    img.set_data(1 - grid)
    fig.canvas.draw_idle()

plt.ioff()
plt.close()
