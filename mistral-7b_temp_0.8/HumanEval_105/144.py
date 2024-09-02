
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
    # Solution 1
    arr = [str(x) for x in arr]
    numbers = 'One Two Three Four Five Six Seven Eight Nine'.split()
    for i in range(len(arr)):
        if arr[i] in numbers:
            arr[i] = numbers[int(arr[i]) - 1]
    return arr

    # Solution 2
    arr = [str(x) for x in arr]
    arr = sorted(arr)
    arr = reversed(arr)
    arr = [int(x) for x in arr]
    numbers = 'One Two Three Four Five Six Seven Eight Nine'.split()
    arr = [numbers[x] for x in arr]
    return arr

    # Solution 3
    arr = [str(x) for x in arr]
    arr = sorted(arr)
    arr = reversed(arr)
    arr = [int(x) for x in arr]
    arr = ['One Two Three Four Five Six Seven Eight Nine'.split()[x] for x in arr]
    return arr
