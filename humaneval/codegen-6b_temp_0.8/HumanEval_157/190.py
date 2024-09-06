
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
    if a >= b + c or b >= c + a or c >= a + b:
        return False
    while a % 2 == 0:
        a = a / 2
    while b % 2 == 0:
        b = b / 2
    while c % 2 == 0:
        c = c / 2
    # Use the right most of each number to check if it can be divided by all other
    # number
    if a % a == 0 and b % b == 0 and c % c == 0:
        return True
    return False
