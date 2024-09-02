
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
    def sort_step(arr, i, j):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
        return
    def reverse_step(arr):
        i = len(arr) - 1
        j = 0
        while j < len(arr):
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
            j += 1
        return
    arr = sorted(arr)
    if len(arr) > 1:
        sort_step(arr, 0, len(arr) - 1)
    return [arr[i:i+1] for i in range(0, len(arr), 1)]