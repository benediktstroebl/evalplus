
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
    try:
        side_a = float(a)
        side_b = float(b)
        side_c = float(c)

        if (side_a > side_b + side_c) or (side_b > side_a + side_c) or (side_c > side_a + side_b):
            return -1

        s = (side_a + side_b + side_c) / 2.0
        return round(math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_
