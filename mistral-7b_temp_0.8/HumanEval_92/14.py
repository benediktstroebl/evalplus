
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
    sum = x+y+z
    # print("Sum:", sum)

    if x == sum and type(x) == int:
        print(x, "equals the sum:", sum)
    elif y == sum and type(y) == int:
        print(y, "equals the sum:", sum)
    elif z == sum and type(z) == int:
        print(z, "equals the sum:", sum)
    else:
        print("No such number exists")


    # return x == sum or y == sum or z == sum

