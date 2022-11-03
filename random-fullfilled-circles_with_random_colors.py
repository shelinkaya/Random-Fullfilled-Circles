#below code draw 100 randomized fullfilled circles with random colors and save as .svg and .json

from random import randint
from svg_turtle import SvgTurtle
import turtle
from turtle import Turtle
import turtle 
import xml.etree.ElementTree as ET
import json
from turtle import Screen

screen= Screen()


def fiber_circle(fiber, width, height):
    fiber_r=25
    fiber_num = 100
    cursor_size = 20
    fiber.hideturtle()
    fiber.speed("fastest")
    fiber.screen.colormode(255)
    
    fiber.screen.bgcolor("white")
    fiber.shape("circle")
    fiber.shapesize(fiber_r / cursor_size)
    fiber.penup()
    fibers = [] 
    
    for _ in range(fiber_num):
        fiber.color(randint(0, 255),randint(0, 255),randint(0, 255))
        fiberr = fiber.clone()
        fiberr.setposition(
            randint(-width / 2, width / 2),
            randint(-height / 2, height / 2),
        )

        while any((a.distance(fiberr) < fiber_r for a in fibers)):
            fiberr.setposition(
                randint(- width / 2, width / 2 ),
                randint(- height / 2, height / 2),
            )
        
        fiberr.stamp()
        
        fibers.append(fiberr) 
def write_file(fiber_circle, filename, width, height):
    fiber = SvgTurtle(width, height)
    
    fiber_circle(fiber, width, height)
    # Convert to svg string
    data = fiber.to_svg()
    
    # get the String data
    root = ET.fromstring(data)
     # loop through all entries
    outfile = {}
    outfile['polygons'] = []
    for child in root:
        # find tag that consits of "polygon"
        if 'polygon' in child.tag:
            outfile['polygons'].append(child.attrib.get('points'))
    with open((filename+".json"),'w') as outjson:
        json.dump(outfile,outjson)


    

    fiber.save_as((filename+".svg"))

def main():
    write_file(fiber_circle, "image15", 500, 500)
    print("Done.")
    
if __name__ == "__main__":
    main()
