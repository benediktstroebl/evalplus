
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

    def is_valid(a,b,c):
        if (a + b) < c or (b + c) < a or (a + c) < b:
            return False
        return True

    if not is_valid(a, b, c):
        return -1

    a2 = b2 = c2 = 0
    a2 = a * a
    b2 = b * b
    c2 = c * c

    s = (a + b + c) / 2

    area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)

    return area

