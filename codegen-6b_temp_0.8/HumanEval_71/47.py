
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
    # calculate the three sides of the triangle
    A = abs(a**2 + b**2 - c**2)**0.5
    B = abs(a**2 + c**2 - b**2)**0.5
    C = abs(b**2 + c**2 - a**2)**0.5
    # ask if the three sides form a valid triangle
    if A + B <= c and B + c <= A and A + c <= B:
        return round(A * B / 2, 2)
    return -1
