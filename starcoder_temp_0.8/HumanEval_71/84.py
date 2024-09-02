
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
    
    # Check whether the sum of any two sides is greater than the third side
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate the area
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # Round the area to 2 decimal places
        area = round(area, 2)
        # Return the area
        return area
    # If the three sides do not make a valid triangle
    else:
        # Return -1
        return -1

