#5:10 PM
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Ground(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            texture = "sand.png",
            model = 'cube',
            collider = 'box',
            scale = (1000,2,1000),
            position = position
        )

class Earth(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            scale = 2500,
            texture = 'sky_earth.png',
            double_sided = True
        )

class Sea(Entity):
    def __init__(self):
        super().__init__(
            model = 'plane',
            position = (0,0,500),
            collider = 'box',
            texture = 'water.png',
            scale = (1000,1,1000)
        )

class Road(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'road.png',
            collider = 'box',
            position = (0,2,455),
            scale = (1000,2,50)
        )

class Building1(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (-15,0,361),
            scale = (80,488,80),
            double_sided = True
        )

class Building2(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (-276,0,243),
            scale = (80,501,80),
            double_sided = True
        )

class Building3(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (122,0,333),
            scale = (80,486,80),
            double_sided = True
        )

class Building4(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (333,0,-76),
            scale = (80,488,80),
            double_sided = True
        )

class Building5(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (87,0,-111),
            scale = (80,488,80),
            double_sided = True
        )

class Building6(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (-111,0,-321),
            scale = (80,488,80),
            double_sided = True
        )

class Building7(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'building.png',
            position = (-78,0,-78),
            scale = (80,488,80),
            double_sided = True
        )

window.fullscreen = True
player = FirstPersonController()

Ground()
Earth()
Sea()
Road()
Building1()
Building2()
Building3()
Building4()
Building5()
Building6()
Building7()

player.position = (-15,20,455)
player.speed = 10 * player.speed
player.jump_height = 8 * player.jump_height
app.run()
