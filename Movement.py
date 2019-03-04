import bge

controller = bge.logic.getCurrentController()
owner = controller.owner
char = bge.constraints.getCharacter(owner)

sensors = owner.sensors

speed = 0.25

if sensors["W"].positive:
    owner.applyMovement([0, speed, 0], True)
    
if sensors["A"].positive:
    owner.applyMovement([-speed, 0, 0], True)

if sensors["S"].positive:
    owner.applyMovement([0, -speed, 0], True)
    
if sensors["D"].positive:
    owner.applyMovement([speed, 0, 0], True)
    
if sensors["Space"].positive:
    char.jump()
