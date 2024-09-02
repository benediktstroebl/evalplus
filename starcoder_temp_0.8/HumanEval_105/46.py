
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

    # Initialize the return value to empty list
    ret = []

    # If the array is empty, return empty list
    if len(arr) == 0:
        return ret

    # Sort the array
    arr.sort()

    # Reverse the array
    arr.reverse()

    # Iterate through each item in the array
    for item in arr:
        # If item is between 1 and 9, append it to return list
        if item >= 1 and item <= 9:
            ret.append(NAMES[item-1])

    # Return the return list
    return ret
