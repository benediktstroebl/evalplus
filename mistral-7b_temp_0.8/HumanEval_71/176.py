
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
    # this is the area of a triangle
    # A = 1/2 * base * height

    # find the largest value of the 3 sides
    longest_side = max(a,b,c)

    # check if the other two sides are smaller than the longest
    if ((a+b) > c) and ((a+c) > b) and ((b+c) > a):
        return round(((longest_side*longest_side)/2), 2)

    return -1
