
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    # create a variable that equals the sum of the other two numbers and store it in a variable
    sum_num = x+y+z

    # if the sum is one of the numbers, then return True
    if (x == sum_num or y == sum_num or z == sum_num) and (x==int(x) and y==int(y) and z==int(z)):
        return True
    else:
        return False



    # 2nd solution

    if (x == y+z or y == x+z or z == x+y) and (x == int(x) and y == int(y) and z == int(z)):
        return True
    else:
        return False
