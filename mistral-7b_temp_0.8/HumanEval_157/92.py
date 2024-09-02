
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
    # code goes here
    # check if each side is greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # check if sum of two sides is greater than third side
    if a + b > c and b + c > a and a + c > b:
        # calculate the sum of squares of the sides
        s = (a ** 2 + b ** 2 + c ** 2) / 2
        # check if the perimeter squared is greater than the sum of squares of the sides
        if s * (s - a) * (s - b) * (s - c) > 0:
            return True
        else:
            return False
    else:
        return False
