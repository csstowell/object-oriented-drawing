"""Example solution."""

import cs1graphics as cg

# Make canvas to draw on
paper = cg.Canvas()

paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')

# Create sun

sun = cg.Circle(50, cg.Point(700, 100))
sun.setFillColor('yellow')
paper.add(sun)

# Create house facade

facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
paper.add(facade)

# Create chimney

chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)

# Create tree

tree = cg.Polygon(cg.Point(150, 220),
                  cg.Point(120, 380),
                  cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)

# Create sunrays

sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635, 165))
sunraySW.setBorderColor('yellow')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)

sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)

sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765, 35))
sunrayNE.setBorderColor('yellow')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)

sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635, 35))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)

# Create grass

grass = cg.Rectangle(800, 300, cg.Point(400, 450))
grass.setFillColor('green')
grass.setBorderColor('green')
grass.setDepth(75) # must be behind house and tree
paper.add(grass)

# START SOLUTION

# Create window

window = cg.Rectangle(50, 70, cg.Point(350, 300))
paper.add(window)
window.setFillColor('black')
window.setBorderColor('red')
window.setBorderWidth(2)
window.setDepth(30)

# Create roof

roof = cg.Polygon(cg.Point(280, 250),
                  cg.Point(520, 250),
                  cg.Point(500, 200),
                  cg.Point(300, 200))
roof.setFillColor('darkgray')
roof.setDepth(30) # in front of facade
paper.add(roof)

# Move chimney to front of roof

chimney.setDepth(20) # in front of roof