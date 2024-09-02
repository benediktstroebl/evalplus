
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
    # edge case: if array is empty
    if len(arr) == 0:
        return []
    # convert arr to string
    str_arr = ""
    for i in range(len(arr)):
        str_arr += str(arr[i])
    # sort the string
    sorted_str = "".join(sorted(str_arr))
    # reverse the string
    sorted_str = sorted_str[::-1]
    # convert string to array of strings
    name_arr = sorted_str.split()
    # convert array of strings to array of names
    result = []
    for i in range(len(name_arr)):
        result.append(name_list[int(name_arr[i])])
    return result

