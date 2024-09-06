
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
    arr_length = len(arr)
    if arr_length == 0:
        return []
    for i in range(arr_length):
        if arr[i] < 0 or arr[i] > 9:
            arr.remove(arr[i])
    arr.sort()
    arr.reverse()
    new_arr = []
    for num in arr:
        if num == 1:
            new_arr.append("One")
        elif num == 2:
            new_arr.append("Two")
        elif num == 3:
            new_arr.append("Three")
        elif num == 4:
            new_arr.append("Four")
        elif num == 5:
            new_arr.append("Five")
        elif num == 6:
            new_arr.append("Six")
        elif num == 7:
            new_arr.append("Seven")
        elif num == 8:
            new_arr.append("Eight")
        elif num == 9:
            new_arr.append("Nine")
    return new_arr
    
