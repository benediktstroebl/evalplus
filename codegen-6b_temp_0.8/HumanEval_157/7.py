
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
    from math import sin, cos, tan, radians, degrees, pi
    def rads(deg):
        return radians(deg)
    try:
        a,b,c = float(a), float(b), float(c)
        abc = a+b+c/2
        half_theta = rads(180/3)
        cos_theta = (bc**2 + abc**2 - bc**2)/(2*bc*abc)
        theta = rads(acos(cos_theta))
        #print(degrees(theta), degrees(half_theta))
        return abs(degrees(theta) - degrees(half_theta)) < 1e-6
    except:
        return False
