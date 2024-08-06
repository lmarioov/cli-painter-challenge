import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center: Point(x, y), radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)
    
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return "Circle with center at ", (self.center.x, self.center.y), " and radius ", (self.radius.r)

class Triangle:
    def __init__(self, point_1, point_2, point_3) -> Point(x, y):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self) -> float:
        sp = (point_1 + point_2 + point_3)/2
        areat = (sp * (sp-point_1) * (sp * point_2)*(sp - point_3))
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return "Triangle with vertices at ", (self.point_1.x, self.point_1.y1), (self.point_2.x, self.point_2.y), " and ", (self.point_3.x, self.point_3.y)

