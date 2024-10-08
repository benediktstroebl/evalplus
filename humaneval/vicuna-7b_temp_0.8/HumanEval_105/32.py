
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
    if not any(str(n) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] for n in arr):
        return ['One']
    n = len(arr)
    result = [f'{name[0]}{n-1}' if n>1 else name[0] for name, n in sorted(zip(arr, range(1,10))) for index, num in enumerate(arr)]
    for i in range(len(result)-1, -1, -1):
        result[i], result[i-1] = result[i-1], result[i]
    return result
