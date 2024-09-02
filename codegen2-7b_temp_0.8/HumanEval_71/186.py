
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
    sum_a = a + b
    sum_b = b + c
    sum_c = a + c
    if sum_a < sum_b and sum_a < sum_c:
        return sum_a / 2
    elif sum_b < sum_a and sum_b < sum_c:
        return sum_b / 2
    elif sum_c < sum_a and sum_c < sum_b:
        return sum_c / 2
    else:
        return -
