
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # make a copy of the original array
    arr_copy = arr.copy()
    # sort the array
    arr_copy.sort()
    # reverse the array
    arr_copy.reverse()
    # sort the array again
    arr_copy.sort()

    # an empty array
    if len(arr_copy) == 0:
        return []
    # a single element
    elif len(arr_copy) == 1:
        return [str(arr_copy[0])]

    # process each element in the array
    for i in range(len(arr_copy)):
        # check to see if the element is between 1 and 9 inclusive
        if (arr_copy[i] >= 1 and arr_copy[i] <= 9):
            # replace each element with its corresponding name
            arr_copy[i] = digits[arr_copy[i] - 1]

    # return the resulting array
    return arr_copy

