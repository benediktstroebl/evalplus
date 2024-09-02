
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    #create a set
    #check to see if the len of the set is the same as the len of the array
    #return the len of the array - the len of the set
    #loop through the array
    #append each number to the set
    #count the len of the set
    #if the count = len of the array, return 0
    #if the count is less than the len of the array, return the len of the array - the count of the set
    setArr = set(arr)
    if len(setArr) == len(arr):
        return 0
    else:
        return len(arr) - len(setArr)


