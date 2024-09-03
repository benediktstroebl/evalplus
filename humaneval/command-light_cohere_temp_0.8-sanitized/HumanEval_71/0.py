import math
def triangle_area(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0  # Return 0 if any side length is zero as triangle with zero sides is not valid
    s = (a + b + c) / 2  # Calculate the semi-perimeter
    return math.sqrt(s) * 2  # Return the area of the triangle using the formula for calculating area of a triangle