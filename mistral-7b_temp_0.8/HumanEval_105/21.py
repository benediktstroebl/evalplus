
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

    if arr:
        arr_length = len(arr)
        if arr_length > 9:
            arr = sorted(arr)
            new_arr = []
            for i in arr:
                if i in range(1, 10):
                    new_arr.append(i)
            new_arr = sorted(new_arr, reverse=True)
            for i in new_arr:
                if i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    new_arr[new_arr.index(i)] = num_to_str(i)
            return new_arr
        else:
            return []

