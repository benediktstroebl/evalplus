
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
    # Find largest side
    largest_side = a
    if b > largest_side:
        largest_side = b
    if c > largest_side:
        largest_side = c
    # Check if triangle is valid
    if largest_side <= (a + b + c - largest_side):
        area = (a * b) / 2
        return round(area, 2)
    else:
        return -1
