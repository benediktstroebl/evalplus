
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    # Your code here
    # 'a' should be less than 'b'
    if a > b:
        a, b = b, a
    # 'a' should be less than 'c'
    if a > c:
        a, c = c, a
    # 'b' should be less than 'c'
    if b > c:
        b, c = c, b

    return a**2 + b**2 == c**2

