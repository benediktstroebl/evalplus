
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
    arr = list(arr)  # convert the array to a list
    if not arr:
        return []
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr) and arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return [arr[i-1] for i in range(len(arr))]