
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
    if len(arr) == 0:
        return []
    res = []
    for n in arr:
        if n >= 1 and n <= 9:
            res.append(str(n))
    res.sort(reverse=True)
    return res

assert([8, 5, 4, 3, 2, 2, 1, 1] == by_length([2, 1, 1, 4, 5, 8, 2, 3]))
assert([] == by_length([]))
assert([8, 5, 4, 3, 2, 2, 1, 1] == by_length([55, 3, -1 , 1]))
assert([1, 1, 2, 2, 3, 4, 5, 8] == by_length([2, 1, 1, 4, 5, 8, 2, 3]))