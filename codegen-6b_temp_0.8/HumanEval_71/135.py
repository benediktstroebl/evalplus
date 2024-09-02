
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
    side_one = float(a)
    side_two = float(b)
    side_three = float(c)
    if side_one + side_two <= side_three or side_one + side_three <= side_two or side_two + side_three <= side_one:
        return -1.00
    return round((side_one * side_two * side_three) / (4 * float((side_one + side_two + side_three) * (side_one - side_two) * (side_two - side_three))), 2)

