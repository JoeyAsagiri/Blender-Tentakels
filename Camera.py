import bge
import GameLogic
import Rasterizer

gameWidth = Rasterizer.getWindowWidth()
gameHeight = Rasterizer.getWindowHeight()

directionXAxis = -1
directionYAxis = -1

controller = bge.logic.getCurrentController()
owner = controller.owner
parent = owner.parent
mouse = controller.sensors['Mouse']

Rasterizer.setMousePosition(int(gameWidth/2), int(gameHeight/2))

sensitivity = 0.0020

mousePositionX = mouse.position[0] - gameWidth/2
mousePositionY = mouse.position[1] - gameHeight/2

#fix mouse drift on subpixel positions
if mousePositionX == -0.5:
    mousePositionX = 0
if mousePositionY == -0.5:
    mousePositionY = 0

rotXAxis = (mousePositionX * directionXAxis) * sensitivity
rotYAxis = (mousePositionY * directionYAxis) * sensitivity

parent.applyRotation([0,0,rotXAxis])

# implement rotation cap on looking up and down
orientation = owner.orientation

if orientation[2].z > -0.90 and rotYAxis > 0:
    owner.applyRotation([rotYAxis,0,0], True)
if orientation[2].z < 0.90 and rotYAxis < 0:
    owner.applyRotation([rotYAxis,0,0], True)

    
