
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
    
    s1 = a + b
    s2 = b + c
    s3 = c + a

    # Use the Heron's Formula
    # 1/2(s1) + 1/2(s2) = 1/2(s3)
    # 1/2(s1)^2 + 1/2(s2)^2 = 1/2(s3)^2
    # 1/2(s1)^2 + 1/2(s2)^2 = 1/2(s3)^2
    # 1/2(s1)^2 + 1/2(s2)^2 = 1/2(s3)^2
    # 1/2(s1)^2 + 1/2(s2)^2 = 1/2(s3)^2
    # (s1)^2 + (s2)^2 = (s3)^2
    # (s1)^2 + (s2)^2 = (s3)^2
    # s1^2 + s2^2 = s3^2
    # s1^2 + s2^2 = s3^2
    # (s1)^2 + (s2)^2 = (s3)^2 = s3^2
    # s1^2 + s2^2 = s3^2
    # s1^2 + s2^2 = s3^2
    # s1^2 + s2^2 = s3^2
    # 4s1^2 = s3^2
    # s1^2 = (s3/2)^2
    # s2^2 = (s3/2)^2
    # (s1/2)^2 + (s2/2)^2 = (s3/2)^2
    # (s1/2)^2 + (s2/2)^2 = (s3/2)^2
    # (s1/2)^2 + (s2/2)^2 = (s3/2)^2
    # s1^2 + s2^2 = (s3/2)^2
    # (s1)^2 + (s