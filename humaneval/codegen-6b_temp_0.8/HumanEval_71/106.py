
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a+b > c and a+c > b and b+c > a:
        s = (a+b+c)/2 # Take average of sides
        return round(sqrt(s*(s-a)*(s-b)*(s-c)), 2)
    else:
        return -1

from test_triangle_area import test_triangle_area
from nose.tools import assert_equal
