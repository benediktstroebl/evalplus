
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
    #create a set of numbers
    nums = {x, y, z}
    #if the number of items in the set is 2 and if all items are integers
    if len(nums) == 2 and all(isinstance(i, int) for i in nums):
        #create a list of items
        items = list(nums)
        #assign first item
        first = items[0]
        #assign second item
        second = items[1]
        #if sum of first and second item is equal to the third item
        if first + second == z:
            #return true
            return True
        #if sum of first and second item is not equal to the third item
        else:
            #return false
            return False
    #else return false
    else:
        return False

