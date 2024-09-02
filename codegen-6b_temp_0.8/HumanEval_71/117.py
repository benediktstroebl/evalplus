
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
    # Returns the area of a Triangle when the three sides make a valid triangle.
    # If any of the sides is not length 3, then -1 is returned.
    # If the sum of two sides is greater than the third side, the area is returned rounded to 2 decimal places

    return round((a + b + c) * (1/2) * (1/2), 2) if a >= 0 or b >= 0 or c >= 0 else -1

