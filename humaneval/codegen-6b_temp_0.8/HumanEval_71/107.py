
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
    s = (a + b + c) / 2
    # Use Heron's formula for the area of a right triangle to solve for the length of the side.
    # Use np.sqrt to square root, then multiply by 2 since a * b * can only be positive.
    return round(np.sqrt(s * (s - a) * (s - b) * (s - c)), 2) if a < s < b + c else -1

