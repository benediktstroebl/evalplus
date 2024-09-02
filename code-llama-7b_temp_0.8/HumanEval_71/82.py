
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
    # Regarding the area of a triangle, the formula is:
    # area = 1/2*base*height
    # base is the length of two sides of the triangle. In our case, we can 
    # set base as the length of two sides that is longer than the third side
    # 
    # we use "is" to check whether two variables are the same. 
    # In python, this is called "is identity".
    # In python, two variables are the same if they point to the same object
    # But in case of primitive data types (int, float, bool, str, etc.), two
    # variables are the same if they have the same values.
    
    # Here is an example of using "is" to check whether two variables point to
    # the same object
    a_is_b = a is b
    print(a_is_b)
    
    # For primitive data types, we need to explicitly check the values of the variables
    # Since we know that the value of c is larger than a and b, we check the values of a and b
    # using >
    if a > b:
        # check if a > c
        a_larger_than_c = a > c
        # check if b > c
        b_larger_than_c = b > c
        # Check whether a, b, and c form a triangle
        if a_larger_than_c and b_larger_than_c:
            # calculate the area
            area = (a + b + c) / 2
            return round(area, 2)
        else:
            return -1
    else:
        return -1
