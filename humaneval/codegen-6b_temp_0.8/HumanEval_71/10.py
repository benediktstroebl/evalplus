
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
    
    if a > b and a+b > c:
        return round(math.fabs(0.5*(a+b)*(c-b)),2)
    elif a > c and a+c > b:
        return round(math.fabs(0.5*(a+c)*(b-c)),2)
    elif b > a and b+a > c:
        return round(math.fabs(0.5*(b+a)*(c-a)),2)
    elif b > c and b+c > a:
        return round(math.fabs(0.5*(b+c)*(a-c)),2)
    elif c > a and c+a > b:
        return round(math.fabs(0.5*(c+a)*(b-a)),2)
    elif c > b and c+b > a:
        return round(math.fabs(0.5*(c+b)*(a-b)),2)
    else:
        return -1
        
    
