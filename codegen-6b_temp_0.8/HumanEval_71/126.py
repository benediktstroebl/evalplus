
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
    
    sides = (a, b, c)
    sums = []
    for side in sides:
        sums.append(side)
    sums.sort()
    if sums[-1] < sums[-2] + sums[-3]:
        side_lengths = [a, b, c]
        sums = []
        for side in side_lengths:
            sums.append(side)
        sums.sort()
        return sums[-1] * sums[-2] / 2
    else:
        return -1

