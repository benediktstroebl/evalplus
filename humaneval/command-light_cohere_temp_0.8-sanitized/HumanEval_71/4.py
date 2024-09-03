import math
def triangle_area(a, b, c):
    # Check for positive side lengths
    if (a < 0 or b < 0 or c < 0):
        return None  # Return None if any side length is negative
    return math.sqrt(a**2 + b**2 + c**2)