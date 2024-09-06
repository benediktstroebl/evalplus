
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
    
    side_1 = a
    side_2 = b
    side_3 = c
    
    side_1 = side_1**2
    side_2 = side_2**2
    side_3 = side_3**2
    
    sum_of_sides = side_1 + side_2 + side_3
    
    if sum_of_sides > side_3:
        return round(sum_of_sides, 2)
    else:
        return -1
    
    
