
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

    #! IF sum of any two sides is greater than the third side then the triangle is valid.
    
    if sum(a, b) > c and sum(b, c) > a and sum(c, a) > b:
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)
    return -1
