
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
    sides = [a, b, c]
    sorted_sides = sorted(sides)
    sum_of_sides = sum(sorted_sides)
    if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
        return sum_of_sides
    return -1


