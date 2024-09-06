
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
    
    def is_right_angle(side1, side2, side3):
        return (side1+side2>=side3 and side1+side3>=side2 and side2+side3>=side1)
    
    return is_right_angle(a,b,c)
