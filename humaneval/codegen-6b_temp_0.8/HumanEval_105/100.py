
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
    # edge case
    if not arr:
        return []

    # sort arr
    arr.sort()

    # create a new list
    new_arr = []

    # traverse the array
    for i in arr:
        # check if i is between 1 and 9
        if 1 <= i <= 9:
            # add the digit to the new array
            new_arr.append(DIGIT_TO_NAME_MAP[i])
        # else ignore the number

    # reverse the array
    new_arr.reverse()

    return new_arr
