
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
    # Return -1 if the three sides do not form a triangle
    if a+b<=c or a+c<=b or b+c<=a:
        return -1
    # Return -1 if the sum of any two sides is less than or equal to the third side
    if a>=b+c or b>=a+c or c>=a+b:
        return -1
    # Return area of the triangle rounded to 2 decimal places
    return round(0.5*a*b*math.sin(math.acos((b*b+c*c-a*a)/(2*b*c))),2)
