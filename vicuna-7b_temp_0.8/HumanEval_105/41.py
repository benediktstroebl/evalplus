
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
    def count(lst):
        if lst == 1:
            return 1
        if lst == 2:
            return 2
        if lst == 3:
            return 3
        if lst == 4:
            return 4
        if lst == 5:
            return 5
        if lst == 6:
            return 6
        if lst == 7:
            return 7
        if lst == 8:
            return 8
        return 0
    n = len(arr)
    if n == 0:
        return []
    result = [0] * (10)
    i = 0
    while i < n:
        count = count(arr[i])
        if count == 0:
            result[count] = arr[i]
            i += 1
        else:
            result[count] += arr[i]
            i += 1
    return result