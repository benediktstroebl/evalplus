
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
    sides = (a,b,c)
    sums = [a + b, b + c, c + a]
    if sums[0] > sums[1] and sums[0] > sums[2] and sums[0]**2 == sums[1]**2 + sums[2]**2: 
        return round((sums[0]**2)*(1/2),2)
    elif sums[1] > sums[2] and sums[1] > sums[0] and sums[1]**2 == sums[2]**2 + sums[0]**2:
        return round((sums[1]**2)*(1/2),2)
    elif sums[2] > sums[0] and sums[2] > sums[1] and sums[2]**2 == sums[0]**2 + sums[1]**2:
        return round((sums[2]**2)*(1/2),2)
    else:
        return -1

