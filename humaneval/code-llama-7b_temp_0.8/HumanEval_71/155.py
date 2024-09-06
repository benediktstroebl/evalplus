
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
    # Verify if it is possible to create a triangle with the given data
    if a + b > c and a + c > b and b + c > a:
        # Given the sides of the triangle, the area can be calculated with the 
        # Heron formula. This formula is derived from the Pythagorean theorem.
        s = (a + b + c) / 2
        return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
    # The Heron formula can only be used when the input data is valid
    return -1
