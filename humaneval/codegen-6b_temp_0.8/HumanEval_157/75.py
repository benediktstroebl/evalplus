
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return ((a ** 2) + (b ** 2) == (c ** 2) or (b ** 2) + (c ** 2) == (a ** 2) or (a ** 2) + (c ** 2) == (b ** 2))

from Test import Test
Test.assertEquals(right_angle_triangle(3, 4, 5), True);
Test.assertEquals(right_angle_triangle(1, 2, 3), False);
Test.assertEquals(right_angle_triangle(1, 1, 1), True);
Test.assertEquals(right_angle_triangle(3, 4, 6), False);
Test.assertEquals(right_angle_triangle(2, 5, 10), True);
Test.assertEquals(right_angle_triangle(1, 2, 3), False);
Test.assertEquals(right_angle_triangle(0, 1, 1), False);
Test.assertEquals(right_angle_triangle(2, 2, 3), True);