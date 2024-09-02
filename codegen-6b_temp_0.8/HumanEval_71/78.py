
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
    # set variables
    side1 = int(min(a, b, c))
    side2 = int(max(a, b, c))
    s = float(side1 + side2) / 2
    area = (s * (s - side1) * (s - side2)) ** 0.5
    return f'{area:.2f}'

