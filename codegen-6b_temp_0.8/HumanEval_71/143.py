
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
    sum_of_sides = a + b + c
    side_lengths = sorted([a, b, c])
    if sum_of_sides < side_lengths[0] + side_lengths[1] or sum_of_sides < side_lengths[1] + side_lengths[0]:
        return -1
    else:
        return round(sum_of_sides / 2, 2)

