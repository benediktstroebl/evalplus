
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
    if not arr:
        return []

    # sort the array
    arr.sort()
    arr.reverse()

    # map each int to a string, return the result
    result = []
    for num in arr:
        if num < 10:
            result.append('One')
        elif num < 100:
            result.append('Two')
        elif num < 1000:
            result.append('Three')
        elif num < 10000:
            result.append('Four')
        elif num < 100000:
            result.append('Five')
        elif num < 1000000:
            result.append('Six')
        elif num < 10000000:
            result.append('Seven')
        elif num < 100000000:
            result.append('Eight')
        elif num < 1000000000:
            result.append('Nine')
    return result

