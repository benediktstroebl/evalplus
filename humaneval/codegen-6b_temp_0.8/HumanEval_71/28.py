
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
    # Triangle area: (S1*S2)/2
    # Triangle area is the area of the triangle's Herons Law Theorem
    return round(((a*b)/2) + ((b*c)/2) + ((c*a)/2), 2)