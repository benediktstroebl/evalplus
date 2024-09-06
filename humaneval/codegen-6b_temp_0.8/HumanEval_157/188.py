
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
    
    try:
        (length_a, length_b, length_c) = (a, b, c)
        length_a /= 2
        if length_a == int(length_a):
            length_a = int(length_a)
        length_b /= 2
        if length_b == int(length_b):
            length_b = int(length_b)
        length_c /= 2
        if length_c == int(length_c):
            length_c = int(length_c)
    except ZeroDivisionError:
        return False
    
    table = {
        (length_a, length_b, length_c): True,
        (length_b, length_a, length_c): True,
        (length_c, length_a, length_b): True,
        (length_c, length_b, length_a): True
    }
    
    for i in table.keys():
        if i == (length_a, length_b, length_c):
            return table.get(i)
        elif i == (length_b, length_a, length_c):
            return table.get(i)
        elif i == (length_c, length_a, length_b):
            return table.get(i)
        elif i == (length_c, length_b, length_a):
            return table.get(i)
        
    return False
