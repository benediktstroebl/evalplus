
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
    # Step 1: Calculate the perimeter
    perimeter = a + b + c

    # Step 2: Calculate the semi-perimeter
    semi_perimeter = perimeter / 2

    # Step 3: Calculate the area
    area = (semi_perimeter * (semi_perimeter - a) * 
            (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

    # Step 4: Round the area to 2 decimal points
    area = round(area, 2)

    # Step 5: Return the area
    return area
