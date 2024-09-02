
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
    # Check if a, b and c are numbers
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number) or not isinstance(c, numbers.Number):
        return -1
    # Check if a, b and c are less than 0 or more than 100
    if not a>0 or not b>0 or not c>0:
        return -1
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c)/2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        area = round(area, 2)
        return area
    else:
        return -1
