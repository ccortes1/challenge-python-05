from math import pi


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return pow(side,2)


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return ((base_minor + base_major )* height)/2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (perimeter * apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return round(2*pi*radius,4)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.side = 2
            self.base = 3
            self.height = 2
            self.diagonal_1 = 2
            self.diagonal_2 = 2
            self.base_minor = 2
            self.base_major = 3
            self.perimeter = 4
            self.apothem = 2
            self.radius = 2


        def test_square_area(self):
            # Make this test first...
            self.assertEqual(square_area(self.side),4)

        def test_rectangle_area(self):
            # Make this test first...
            self.assertEqual(rectangle_area(self.base, self.height), 6)

        def test_triangle_area(self):
            # Make this test first...
            self.assertEqual(triangle_area(self.base, self.height), 3)

        def test_rhombus_area(self):
            # Make this test first...
            self.assertEqual(rhombus_area(self.diagonal_1, self.diagonal_2), 2)

        def test_trapezoid_area(self):
            # Make this test first...
            self.assertEqual(trapezoid_area(self.base_minor, self.base_major, self.height), 5)

        def test_regular_polygon_area(self):
            # Make this test first...
            self.assertEqual(regular_polygon_area(self.perimeter, self.apothem), 4)

        def test_circumference_area(self):
            # Make this test first... 
            self.assertEqual(circumference_area(self.radius), 12.5664)


        def tearDown(self):
            # Delete the needed values for the tests
            del(self.side)
            del(self.base)
            del(self.height)
            del(self.diagonal_1)
            del(self.diagonal_2)
            del(self.base_minor)
            del(self.base_major)
            del(self.perimeter)
            del(self.apothem)
            del(self.radius)

    unittest.main()
