#Exercise 01 - 
import numpy as np
state01 = 910

#Action => s' = f(s,a)
#
def position: [(00,01)]

#Funções


def traject (position):
    #Up 
    def state = state01

    action = actionRandom.random.radint(0,3)
    actionRobot (action)
    if up: 
        checkWall()

def actionRobot (action):
    switch(action){
        case "up": 
            return [(0,1)]
        case 1: 
            return "down"
        case 2: 
            return "left"
        case 3: 
            return "right"
    };

def actionRandom(a){
    switch(a){
        case 0: 
            return "up"
        case 1: 
            return "down"
        case 2: 
            return "left"
        case 3: 
            return "right"
    };
};
[0,1][-1,1]

def checkWall(yNow, xNow, yFuture, xFuture):
    if (yFuture < 0) or (yFuture > 9):
        yNew= yNow
    else: yNew=yFuture,

    if (xFuture < 1) or (xFuture > 10):
        xNew=xNow
    else: xNew=xFuture
    return (yNew, xNew)
