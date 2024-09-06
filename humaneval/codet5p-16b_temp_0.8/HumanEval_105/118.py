
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

    arr = sorted(list(set(arr)))
    n = len(arr)
    arr = [str(i) for i in arr]
    if n == 0:
        return []
    if n == 1:
        return ["One"]
    if n == 2:
        return ["One", "Two"]
    if n == 3:
        return ["One", "Two", "Three"]
    if n == 4:
        return ["One", "Two", "Three", "Four"]
    if n == 5:
        return ["One", "Two", "Three", "Four", "Five"]
    if n == 6:
        return ["One", "Two", "Three", "Four", "Five", "Six"]
    if n == 7:
        return ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    if n == 8:
        return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
    if n == 9:
        return ["One", "Two", "Three", "Four", "Five
