class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 49 or self.height > 49:
            return "Too big for picture."
        else:
            string = ''
            for n in range(self.height):
                if n < self.height:
                    string += '*' * self.width + '\n'
                else:
                    string += '*' * self.width

        return string

    def get_amount_inside(self, polygon):
        how_many = (self.width // polygon.width) * \
            (self.height // polygon.height)
        return how_many


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, width):
        super().set_width(width)
        self.height = width
        self.side = width

    def set_height(self, height):
        super().set_height(height)
        self.width = height
        self.side = height
