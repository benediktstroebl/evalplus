
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
    # If any side is 0, the triangle doesn't exist
    if any(side == 0 for side in [a, b, c]):
        return -1
    
    # If two sides are equal, the triangle doesn't exist
    if abs(a - b) == 0:
        return -1
    
    # If all sides are equal, the triangle is a right triangle
    if abs(a - c) == abs(b - c):
        return (a * sqrt(3)) / 4
    
    # If the sum of any two sides is greater than the third side, the triangle is a right triangle
    if abs(a + b) > c or abs(b + c) > a or abs(c + a) > b:
        return (a * sqrt(3)) / 4
    
    # If the sum of any two sides is less than the third side, the triangle doesn't exist
    if abs(a + b) < c or abs(b + c) < a or abs(c + a) < b:
        return -1
    
    # Calculate the area of the triangle
    area = (a + b + c) * (sqrt(a * a + b * b) + sqrt(c * c + a * a)) / 2
    
    # Round the area to 2 decimal places
    return round(area, 2)
