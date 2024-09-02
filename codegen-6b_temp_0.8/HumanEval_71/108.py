
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
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    else:
        return round((a + b + c) * 0.5, 2)

'''
Valid Triangle:
Given three integers A, B, C, determine if there is a triangle that 
cuts a line through A, B, and C, and has a parallel side. Return 1 if it exists.
If not exist, return 0.
Example:
Valid Triangle?
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 1:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 0:
Valid Triangle? 1:
Valid Triangle? 1:
Valid Triangle? 0:
Valid Triangle? 0:
Valid Triangle? 0:
valid Triangle? 1:
valid Triangle? 1:
valid Triangle? 0:
valid Triangle? 0:
valid Triangle? 0:
valid Triangle? 1:
valid Triangle? 1:
valid Triangle? 0:
valid Triangle? 0:
valid Triangle? 0:
'''
