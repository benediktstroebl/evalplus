
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
        return arr

    arr = sorted(arr)

    arr_length = len(arr)
    index = 1

    while arr_length > 1:
        # 2, 1, 3, 4, 5, 6, 7, 8, 9
        if arr[index] == 1:
            arr[index] = "One"
            index += 1
        elif arr[index] == 2:
            arr[index] = "Two"
            index += 1
        elif arr[index] == 3:
            arr[index] = "Three"
            index += 1
        elif arr[index] == 4:
            arr[index] = "Four"
            index += 1
        elif arr[index] == 5:
            arr[index] = "Five"
            index += 1
        elif arr[index] == 6:
            arr[index] = "Six"
            index += 1
        elif arr[index] == 7:
            arr[index] = "Seven"
            index += 1
        elif arr[index] == 8:
            arr[index] = "Eight"
            index += 1
        elif arr[index] == 9:
            arr[index] = "Nine"
            index += 1
        arr_length -= 1

    arr = arr[::-1]

    return arr
