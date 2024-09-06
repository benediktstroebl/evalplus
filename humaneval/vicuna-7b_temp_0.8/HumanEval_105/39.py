
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
    def count_by_length(arr):
        # check the first two digits
        if arr[0] == 1 and arr[1] == 1:
            return ["One"]
        if arr[0] == 2 and arr[1] == 1:
            return ["Two"]
        if arr[0] == 1 and arr[1] == 2:
            return ["One"]
        if arr[0] == 2 and arr[1] == 2:
            return ["Two"]
        if arr[0] == 3 and arr[1] == 1:
            return ["Three"]
        if arr[0] == 4 and arr[1] == 1:
            return ["Four"]
        if arr[0] == 1 and arr[1] == 3:
            return ["One"]
        if arr[0] == 2 and arr[1] == 3:
            return ["Two"]
        if arr[0] == 3 and arr[1] == 2:
            return ["Three"]
        if arr[0] == 4 and arr[1] == 2:
            return ["Four"]
        if arr[0] == 1 and arr[1] == 4:
            return ["One"]
        if arr[0] == 2 and arr[1] == 4:
            return ["Two"]
        if arr[0] == 3 and arr[1] == 4:
            return ["Three"]
        if arr[0] == 4 and arr[1] == 1:
            return ["Four"]
        return []
    
    # use recursion
    if len(arr) > 0:
        # check the last digit
        if arr[-1] == 1:
            return by_length(arr[:-1]) + [arr[-1]] + by_length(arr[1:])
        if arr[-1] == 2:
            return by_length(arr[:-1]) + [arr[-1]] + by_length(arr[1:])
        if arr[-1] == 3:
            return by_length(arr[:-1]) + [arr[-1]] + by_length(
