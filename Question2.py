# -*- coding: utf-8 -*-


from pylab import *

#question b

#simulation parameters


D = 2 #Diffusion constant
dt = 0.0001 #time discretization
L = 10 #length of domain

N = 100 #number of discrete points

x = linspace(-L/2,L/2,N) #x coordinate
dx = x[1] - x[0] #space discretization

k = D*dt/dx**2
conc = np.zeros(N) #concentration at current time step
conc1 = np.zeros(N) #conccentration at next time step

#setting up intial conditions

conc[N/2-5:N/2+5] = 10 #concentration of chemical 
plt.figure(1)
plt.plot(x,conc)

#Diffuse stuff

for t in range(1,200): #t is time step
    
    for i in range(1,N-1): #i is index on x
        
        conc1[i] = conc[i] + (conc[i-1] - 2*conc[i] + conc[i+1])*k

    conc = conc1[:]



plt.figure(2)
plt.plot(x,conc)
        
        
        



