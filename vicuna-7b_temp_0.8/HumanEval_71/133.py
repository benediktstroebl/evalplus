
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
    # Check if the three sides form a valid triangle
    if (a + b > c) and (b + c > a) and (c + a > b):
        # Convert sides to meters
        a = a * 1000 # meters
        b = b * 1000 # meters
        c = c * 1000 # meters
        
        # Calculate the area using Heron's formula
        return 0.5 * ((a + b + c) / 2) * (a + b + c) / 3
    else:
        return -1
