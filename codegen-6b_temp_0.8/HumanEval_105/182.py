
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
    # handle empty array
    if len(arr) == 0:
        return []
    # sort the array
    arr.sort(reverse=True)
    result = []
    # reversed the numbers
    arr = list(reversed(arr))
    # loop over each number in array
    for num in arr:
        # handle invalid numbers
        if num < 1 or num > 9:
            continue
        # do the calculations
        ones, tens = divmod(num, 10)
        twenties, tens = divmod(tens, 10)
        tens = str(tens)
        if ones == 1:
            result += ["One"]
        elif ones == 2:
            result += ["Two"]
        elif ones == 3:
            result += ["Three"]
        elif ones == 4:
            result += ["Four"]
        elif ones == 5:
            result += ["Five"]
        elif ones == 6:
            result += ["Six"]
        elif ones == 7:
            result += ["Seven"]
        elif ones == 8:
            result += ["Eight"]
        elif ones == 9:
            result += ["Nine"]
        # if each number is duplicated, then ignore it
        if ones in result:
            continue
        # if duplicate number in arr, then ignore it
        elif len(result) > 1:
            result += [""]
    # join result
    return [str(x) for x in result]
