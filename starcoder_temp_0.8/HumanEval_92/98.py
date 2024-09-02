
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
    l = [x, y, z]
    for i in range(len(l)):
        if type(l[i]) == int:
            l[i] = l[i]
        else:
            l[i] = int(l[i])
    for j in range(len(l)):
        if (l[j] == sum(l[0:2]) or l[j] == sum(l[1:3])) and l[j]!= sum(l):
            return True
    return False


