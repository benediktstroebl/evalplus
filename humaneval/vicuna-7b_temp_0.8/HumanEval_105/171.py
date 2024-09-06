
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
    from random import choice, random
    if not arr:
        return []
    if len(arr) == 1:
        if str(arr[0]) in ['-1', '1']:
            return ['One']
        return ['One']
    n = len(arr)
    digits = set(str(x) for x in arr)
    digits = sorted(digits)
    for i in range(n-1, -1, -1):
        digits.remove(digits.pop())
    digits.append(digits.pop())
    result = []
    for d in digits:
        result.append(choice(list(digits.keys()) + ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]))
    return result
