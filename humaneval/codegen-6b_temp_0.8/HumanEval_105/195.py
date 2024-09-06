
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
    # YOUR CODE HERE
    len_arr = len(arr)
    
    if len_arr == 0:
        return []
    
    if len_arr == 1:
        return [str(arr[0])]
    
    arr = sorted(arr)
    arr.reverse()
    
    ret_arr = []
    
    for i in xrange(len_arr):
        if arr[i] < 10 and arr[i] > 0:
            ret_arr.append(str(arr[i]))
        else:
            ret_arr.append(digit_to_name(arr[i]))
    
    return ret_arr

