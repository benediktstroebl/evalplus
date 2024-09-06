
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
    # Assign values to a, b, and c
    a, b, c = (float(a), float(b), float(c))
    # Create a new variable named area
    area = 0
    # Determine which side is greater
    if a > b:
        if a < c:
            area = (a * (c - b)) / 2
        elif b > c:
            area = (a * (b - c)) / 2
    elif b > a:
        if b < c:
            area = (b * (c - a)) / 2
        elif a > c:
            area = (b * (a - c)) / 2
    elif c > a:
        if c < b:
            area = (c * (b - a)) / 2
        elif a == b:
            area = (c * (a - b)) / 2
    # Return values rounded to 2 decimal points
    return round(area, 2)
