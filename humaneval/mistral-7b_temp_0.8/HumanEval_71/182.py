
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
    # Print each value
    print(a, b, c)

    # Check to make sure each side is greater than 0
    if a < 0 or b < 0 or c < 0:
        return -1

    # Check for valid triangle
    if (a + b) > c and (b + c) > a and (a + c) > b:
        # Calculate area
        area = (a * b) / 2

        # Round area
        area = round(area, 2)

        # Return area
        return area
    else:
        # Return -1
        return -1
