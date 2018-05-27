#Module for SenseHat Hardware
#Module for implementing time.
from sense_hat import SenseHat
from time import sleep

#BluePrint for all mazes generic class structure


class Maze:
    #python constructor
    def __init__(self, grid, x, y, gems):                                           #Initializing data values
        self.grid = grid
        self.x = x
        self.y = y
        self.gemcheck = gems
    #function to check to see if all gems have been collected
    def check_gems(self,gemss,gem_x,gem_y):                                         #Function to check if you have all the gems
        self.gemss = gemss
        if self.gemcheck == self.gemss:
            gemgrab = True                                                              
            if self.grid[gem_y][gem_x] == e and gemgrab == True:
                return True
        else:
            return False
    #function to check to see if new coordinates will hit a wall
    def check_wall(self,c,d,new_x,new_y):                                           #Function to check the border
    
        if self.grid[new_y][new_x] != border:
            return new_x, new_y
        elif self.grid[new_y][c] != border:
            return c, new_y
        elif self.grid[d][new_x] != border:
            return new_x, d
        else:
            return c,d
    #function takes starting coordinates and works with pitch and roll
    #through gyroscope to determine end coordinates
    def move_marble(self,pitch, roll, c, d):                                        #Function to move the marble
        new_x = c
        new_y = d
        if 1 < pitch < 179 and c != 1:
            new_x -= 1
        elif 181 < pitch < 359 and c != 6:
            new_x += 1
        if 1 < roll < 179 and d != 6:
            new_y += 1
        elif 181 < roll < 359 and d != 1:
            new_y -= 1
        new_x, new_y = self.check_wall(c,d,new_x,new_y)
        return new_x, new_y
    #starts the game by initilizing the maze on the SenseHat 8x8 matrix.
    def startgame(self):                                                            #Function that starts the maze
        gameover = False
        restart = True
        gemgrab = False
        gemss = 0
        while gameover == False:
            orient = sense.get_orientation()
            pitch = orient["pitch"]
            roll = orient["roll"]
            self.x, self.y = self.move_marble(pitch,roll,self.x, self.y)
            if self.grid[self.y][self.x] == f:                                       #if ball rolls over a gem(f)
                gemss += 1
            self.check_gems(gemss,self.x,self.y)
            if self.check_gems(gemss,self.x,self.y) == True:
                gameover = True
                return True                                                        #if i equals the number of gems in the grid
            self.grid[self.y][self.x] = ball
            sense.set_pixels(sum(self.grid,[]))
            sleep(0.20)
            if self.grid[self.y][self.x] == g:
                self.grid[self.y][self.x] = g
            else:
                self.grid[self.y][self.x] = e
            
sense = SenseHat()     #variable link to function

b = (0,0,100) #RGB color values
g = (0,0,0)
ball = (255,51,51)
e = (20,20,20)
f = (0,255,0)
end = e
portal = f
border = b
path = g

#two-dimensional array data structures
#using one letter represention to account for which color the pixel is going to
#be. Looks nicer then a full word ie Blue, Green.

unicornmaze =  [[b,b,b,b,b,b,b,b],
                [b,g,b,g,g,g,f,b],
                [b,g,g,g,b,b,g,b],
                [b,b,b,b,g,g,g,b],
                [b,b,g,g,g,b,b,b],
                [b,g,g,g,g,g,b,b],
                [b,f,b,b,b,g,f,b],
                [b,b,b,b,b,b,b,b]]

fairymaze = [[b,b,b,b,b,b,b,b],
             [b,g,g,g,g,g,g,b],
             [b,b,b,b,b,b,g,b],
             [b,g,g,f,f,b,g,b],
             [b,g,b,f,f,b,g,b],                                         
             [b,g,b,b,b,b,g,b],
             [b,g,g,g,g,g,g,b],
             [b,b,b,b,b,b,b,b]]

phoenixmaze =  [[b,b,b,b,b,b,b,b],
                [b,g,b,f,b,f,b,b],
                [b,g,g,g,g,g,g,b],
                [b,b,b,b,b,b,g,b],
                [b,g,b,b,b,b,g,b],
                [b,g,g,g,g,g,g,b],
                [b,f,b,f,b,f,b,b],
                [b,b,b,b,b,b,b,b]]

dragonmaze =   [[b,b,b,b,b,b,b,b],
                [b,g,b,b,b,b,f,b],
                [b,g,g,g,g,g,g,b],
                [b,b,b,g,g,b,g,b],                                                      # Two Dimensional Array Structures for Mazes
                [b,b,b,g,g,g,g,b],
                [b,f,b,g,b,b,g,b],
                [b,g,g,g,b,f,g,b],
                [b,b,b,b,b,b,b,b]]

puppetmaze =   [[b,b,b,b,b,b,b,b],
                [b,g,b,f,b,f,g,b],
                [b,g,g,g,b,b,g,b],
                [b,b,b,g,g,g,g,b],
                [b,f,g,f,b,b,g,b],
                [b,g,b,g,g,g,g,b],
                [b,f,g,f,g,b,f,b],
                [b,b,b,b,b,b,b,b]]

wizardmaze = [[b,b,b,b,b,b,b,b],
                 [b,b,g,g,g,g,b,b],
                 [b,g,g,b,b,f,g,b],
                 [b,b,b,b,b,b,g,b],
                 [b,g,g,f,b,b,g,b],
                 [b,g,b,b,b,b,g,b],
                 [b,g,g,g,g,g,f,b],
                 [b,b,b,b,b,b,b,b]]

lionmaze =     [[b,b,b,b,b,b,b,b],
                [b,g,g,f,b,g,b,b],
                [b,g,b,g,g,g,b,b],
                [b,g,b,b,b,b,b,b],
                [b,g,g,f,b,f,g,b],
                [b,g,b,b,b,b,g,b],
                [b,g,g,g,g,g,g,b],
                [b,b,b,b,b,b,b,b]]

trollmaze =    [[b,b,b,b,b,b,b,b],
                [b,g,g,b,g,g,f,b],
                [b,b,g,b,g,b,b,b],
                [b,f,g,b,g,f,b,b],
                [b,b,g,b,g,b,b,b],
                [b,b,g,g,g,g,f,b],
                [b,b,f,b,f,b,b,b],
                [b,b,b,b,b,b,b,b]]

#Maze class defined as Maze(mazegrid, start x coordinate, start y coordinate, path color, border color)
#ball doesnt change color
#end point doesnt change color

#Setting up initial objects from main class Maze

unicornmaze = Maze(unicornmaze, 1, 1,3)
fairymaze = Maze(fairymaze, 1, 1,4)                             #Creating Objects from Maze Class
phoenixmaze = Maze(phoenixmaze, 1, 1,5)
dragonmaze = Maze(dragonmaze, 1, 1,3)
puppetmaze = Maze(puppetmaze, 1, 1, 7)
wizardmaze = Maze(wizardmaze, 1, 2, 3)
lionmaze = Maze(lionmaze, 5, 1, 3)
trollmaze = Maze(trollmaze, 1, 1, 6)


maze_catalog = [fairymaze, wizardmaze, lionmaze, unicornmaze, phoenixmaze, trollmaze, puppetmaze, dragonmaze]         #Array of Maze objects


for i in range(len(maze_catalog)):
    maze_catalog[i].startgame()                     #For Loop to go threw each maze
sense.show_message("Winner!")
        
        


