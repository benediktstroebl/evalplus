
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

    arr.sort()
    arr = arr[::-1]

    arr_str = []
    for num in arr:
        if num < 10 and num > 0:
            if num == 1:
                arr_str.append("One")
            elif num == 2:
                arr_str.append("Two")
            elif num == 3:
                arr_str.append("Three")
            elif num == 4:
                arr_str.append("Four")
            elif num == 5:
                arr_str.append("Five")
            elif num == 6:
                arr_str.append("Six")
            elif num == 7:
                arr_str.append("Seven")
            elif num == 8:
                arr_str.append("Eight")
            elif num == 9:
                arr_str.append("Nine")
        else:
            continue

    return arr_str

