
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
    result = []
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [str(arr[0])]
    elif 1 <= arr[0] <= 9 and 1 <= arr[-1] <= 9:
        for digit in range(len(arr)):
            result.append(str(arr[digit]))
        result.sort()
        for i in range(len(arr)-1, -1, -1):
            result[i] = chr(ord('A') + arr[i] - 1)
        return result
    else:
        return by_length(arr[1:-1]) + [arr[-1]]
