
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
    n = 0
    arr_sorted = []
    for element in arr:
        if element >= 1 and element <= 9:
            arr_sorted.append(element)
        elif n == len(arr)-1:
            arr_sorted.append(arr[n])
            n += 1
        elif n == len(arr)-2:
            arr_sorted.append(arr[n])
            n += 1
            arr_sorted.append(arr[n])
        else:
            pass
    
    # replace each number with its name
    return [name_mapping[i] for i in arr_sorted]
