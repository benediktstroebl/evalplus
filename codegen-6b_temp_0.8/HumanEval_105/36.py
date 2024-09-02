
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
    sorted_arr = sorted(arr)
    arr_len = len(arr)

    if arr_len == 0:
        return []

    if arr_len == 1:
        if arr[arr_len - 1] > 9:
            return []
        else:
            return ["One"]

    if arr_len == 2:
        if arr[arr_len - 1] > 9:
            return ["One", "One"]
        elif arr[0] == 1 and arr[1] == 1:
            return ["One", "One"]
        else:
            return ["One", "Two"]

    if arr_len == 3:
        if arr[arr_len - 1] == 1 or arr[arr_len - 2] == 1:
            return ["One", "Two", "Three"]
        else:
            return ["One", "Two", "Three", "One"]

    if arr_len == 4:
        if arr[arr_len - 1] == 1 or arr[arr_len - 2] == 1:
            return ["One", "Two", "Three", "Four"]
        else:
            return ["One", "Two", "Three", "Four", "One"]

    if arr_len == 5:
        if arr[arr_len - 1] == 1 or arr[arr_len - 2] == 1:
            return ["One", "Two", "Three", "Four", "Five"]
        elif arr[arr_len - 1] == 2 or arr[arr_len - 2] == 2:
            return ["Two", "Two", "Three", "Four", "Five"]
        else:
            return ["One", "Two", "Three", "Four", "Five", "One"]

    if arr_len == 6:
        if arr[arr_len - 1] == 1 or arr[arr_len - 2] == 1:
            return ["One", "Two", "Three", "Four", "Five", "Six"]
        else:
            return ["One", "Two", "Three", "Four", "Five", "Six", "One"]

    if arr_len == 7:
        if arr[arr_len - 1] == 1 or arr[arr_len - 2