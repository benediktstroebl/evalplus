
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
    def is_triangle(a, b, c):
        return a < b + c and b < a + c and c < a + b
    
    def is_valid(number):
        return number >= 0
    
    if is_triangle(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2) if is_valid(area) else -1
    return -1
    
