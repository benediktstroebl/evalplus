
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
    # 1. create a list of all numbers and convert each element to integer
    list_numbers = [x, y, z]
    list_numbers_int = [int(i) for i in list_numbers]
    
    # 2. check if one of the elements is equal to the sum of the other two and return the result
    if any(list_numbers_int.count(i) > 1 for i in list_numbers_int):
        return True
    else:
        return False

