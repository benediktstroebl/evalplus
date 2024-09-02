
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

    # sum all the lengths together
    # if the sum is greater than any of the individual lengths, return the area
    # otherwise, return -1
    total = a + b + c
    if total > a and total > b and total > c:
        s = total / 2
        return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
    else:
        return -1
