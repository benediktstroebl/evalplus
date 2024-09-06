
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
    # Write your code here
    s1 = a + b
    s2 = a + c
    s3 = b + c

    if s1 > a and s1 > b and s1 > c:
        area = (a*b*c)/2
        return round(area, 2)
    elif s2 > a and s2 > b and s2 > c:
        area = (a*b*c)/2
        return round(area, 2)
    elif s3 > a and s3 > b and s3 > c:
        area = (a*b*c)/2
        return round(area, 2) 
    else:
        return -1
