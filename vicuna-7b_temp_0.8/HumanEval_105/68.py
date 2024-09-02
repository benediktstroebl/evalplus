
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
    n = 0
    arr_reversed = sorted(arr[::-1], reverse=True)
    n_arr = len(arr_reversed)
    result = []
    for i in range(n_arr):
        result.append(arr_reversed[i])
        if arr_reversed[i] >= 1 and arr_reversed[i] <= 9:
            if arr_reversed[i] > 5:
                name = f"{str(arr_reversed[i])}{' '}{str(arr_reversed[i-1])}{' '}{str(arr_reversed[i-2])}"
            else:
                name = f"{str(arr_reversed[i])}{' '}{str(arr_reversed[i-1])}"
            result.append(name)
    return result