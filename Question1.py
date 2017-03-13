# -*- coding: utf-8 -*-


from pylab import *

#generate seed based on current time

seed()

#simulation parameters

steps = 100 #will change this to a higher number while answering the question

#create a random walker

walk_x = linspace(0,0,steps); walk_y = linspace(0,0,steps); #x and y locations of the random walker




for i in range(1,steps):

    dir_x = rand()-0.5; dir_y = rand()-0.5; #generate random x and y coordinates to advance your walker
    
    norm_dir_x = dir_x/(sqrt(dir_x**2 + dir_y**2)); norm_dir_y = dir_y/(sqrt(dir_x**2 + dir_y**2)); #nomralized direction
    
    
    #Now, advance walker
    
    walk_x[i] = walk_x[i-1] + norm_dir_x
    walk_y[i] = walk_y[i-1] + norm_dir_y


plt.plot(walk_x,walk_y) #initial test that random walker works

