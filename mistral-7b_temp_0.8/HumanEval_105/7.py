
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
    if not all(isinstance(i, int) and 1 <= i <= 9 for i in arr):
        return [str(i) if i % 10 in range(1, 9) else '' for i in arr]

    i = 0
    while i < len(arr):
        if 1 <= arr[i] <= 9:
            arr[i] = (9 - arr[i]) * (-1)
            i += 1
        else:
            i += 1

    i = 0
    while i < len(arr):
        if arr[i] < 0:
            arr[i] = arr[i] * (-1)
            i += 1
        else:
            i += 1

    return [str(i) if i % 10 in range(1, 9) else '' for i in arr]

