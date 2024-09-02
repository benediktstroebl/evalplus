
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
    # Rounding to 2 decimals
    a, b, c = map(lambda x: round(x, 2), [a, b, c])

    # We can't have a negative side
    if a > b + c:
        return -1

    # We can't have a max side above 180
    if a + b > c and a + c > b and b + c > a:
        return round(0.5 * (a * b - c * c), 2)
