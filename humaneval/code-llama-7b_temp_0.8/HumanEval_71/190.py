
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
    # EXAMPLE 1
    # my_string = 'abc'
    # my_string[0]
    # my_string[0:2]
    # my_string[:2]
    # my_string[1:]
    # my_string[1::2]
    # my_string[:1:2]
    # my_string[::2]
    # my_string[::-1]
    # 'hellO'[::-1]
    # 'hello'[::2]
    # 'hello'[::3]
    # 'hello'[::-3]
    # 'hello'[1:3:2]
    # 'hello'[1::2]
    # 'hello'[::-2]
    # 'hello'[::-3]
    # 'hello'[::-4]
    # 'hello'[::-5]
    # 'hello'[::-6]
    # 'hello'[1:-1:2]
    # 'hello'[1::-2]
    # 'hello'[::-3]
    # 'hello'[::-4]
    # 'hello'[::-5]
    # 'hello'[::-6]
    # 'hello'[1:-1:2]
    # 'hello'[1::-2]
    # 'hello'[::-3]
    # 'hello'[::-4]
    # 'hello'[::-5]
    # 'hello'[::-6]

    if a + b <= c:
        return -1
    elif b + c <= a:
        return -1
    elif a + c <= b:
        return -1
    else:
        return 0.5 * ((a + b) * (b + c) * (c + a)) ** 1/2
    
    return 0
