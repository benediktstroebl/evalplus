
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
    # Return -1 if the sides do not form a valid triangle
    if not (a > b or a > c or b > c):
        return -1
    # Return the area of the triangle if the sides form a valid triangle
    else:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        area = round(area, 2)
        return area

    # Another method - Slightly more correct, but slower
    if a + b + c == 0:
        s = 0
    else:
        s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
