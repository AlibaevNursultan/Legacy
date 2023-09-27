class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]


    def inputSides(self):
        self.sides = [float(input("Введите сторону " + str(i+1)+ " : ")) for i in range(self.n)]


    def dispSides(self):
        for i in range(self.n):
            print("Сторона", i+1, " — ", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s* (s-a) * (s-b) * (s-c)) ** 0.5
        print('Площадь треуольника равна %0.2f' % area)
