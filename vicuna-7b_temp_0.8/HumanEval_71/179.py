
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
    if (a + b > c):
        a_sum = a + b
        c_sum = c
        b_sum = a + c
        if (b_sum > c_sum):
            area = (a_sum * c_sum) / 4
            return area
    elif (b + c > a):
        b_sum = b + c
        c_sum = a
        a_sum = b + c
        if (a_sum > c_sum):
            area = (b_sum * c_sum) / 4
            return area
    else:
        return -1
