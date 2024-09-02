
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
    # Xe ly triangulate có thể nghịch đến ở đây
    # A = b * h / 2, 
    # C = c * h / 2, 
    # D = A + C
    # 
    # Trả về A, C của a, b, c bằng 2, nghịch đến giữa của a, b, c
    try:
        a, b, c = float(a), float(b), float(c)
        d = a + b + c
        if d > 2 * (a + c) or d < a + b or d < b + c:
            return -1
        else:
            return round((a * c) / 2, 2)
    except TypeError:
        print('Not a number')

