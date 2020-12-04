import requests
import json
import random
from turtle import *




with open("destinations.txt", "r") as destinations:
    lines = destinations.read().splitlines()

leicester_towns = []

for line in lines:
    line = line.split(", ")
    dest = {'destination': None, 'coords': None}
    dest['destination'] = line[0]
    dest['coords'] = line[1]
    leicester_towns.append(dest)

screen = Screen()
screen.title("Pizza Delivery")
turtle = Turtle()
turtle.speed(10)
screen.colormode(255)
turtle.penup()
turtle.pensize(2)

style = ("Arial", 15, "bold")

for i in range(0, len(leicester_towns)):
    if leicester_towns[i]['destination'] == "City Centre":
        temp = leicester_towns[i]['coords']
        temp = temp.split(",")
        central_coordsX = float(temp[0])
        central_coordsY = float(temp[1])
        
        central_coords = (central_coordsX,central_coordsY)
        
for town in leicester_towns:
    colour = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    penup()
    
    
    if town['destination'] == "City Centre":
        turtle.goto(0,0)
        turtle.dot(20, colour)
        turtle.forward(-5)
        turtle.write(town['destination'], font=style, align='center')
        turtle.forward(5)
    else:
        town_coords = town['coords'].split(",")
        town_coordsX = float(town_coords[0])
        town_coordsY = float(town_coords[1])
        x = (town_coordsX - central_coordsX) * 5000
        y = (town_coordsY - central_coordsY) * 5000
        town_coords = (x,y)
        turtle.goto(town_coords)
        turtle.dot(20, colour)
        turtle.forward(-5)
        turtle.write(town['destination'], font=style, align='center')
        turtle.forward(5)

##        pendown()
##        turtle.pencolor("black")
        

source = screen.textinput("Start", "Starting Point:")
destination = screen.textinput("Destination","Destination:")

for i in range(0, len(leicester_towns)):
    if leicester_towns[i]['destination'] == source:
        sourceCoords = leicester_towns[i]['coords']

    if leicester_towns[i]['destination'] == destination:
        destinationCoords = leicester_towns[i]['coords']

routeAPIcall = "https://api.tomtom.com/routing/1/calculateRoute/\
" + sourceCoords + ":" + destinationCoords + "/json?\
instructionsType=text&language=en-GB\
&vehicleHeading=90&sectionType=traffic\
&report=effectiveSettings&routeType=eco\
&traffic=true&avoid=unpavedRoads\
&travelMode=car&vehicleMaxSpeed=120\
&vehicleCommercial=false&vehicleEngineType=combustion\
&key=vFSnW5hXJm6lFuFOfyyTdkNqWMisO0sj"

routes = requests.get(routeAPIcall)

routes = routes.text
routes = json.loads(routes)



    

distance = round((routes['routes'][0]['summary']['lengthInMeters'] / 1000), 2)

turtle.goto(400, 100)
turtle.write("Shortest Distance: " + str(distance), align='center', font=style)
