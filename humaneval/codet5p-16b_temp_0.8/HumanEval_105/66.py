
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

    if arr == []:
        return []
    
    strarr = sorted(arr, key=str)
    reverse_strarr = strarr[::-1]
    
    return_list = []
    for i in range(len(reverse_strarr)):
        if 1 <= reverse_strarr[i] <= 9:
            return_list.append(str(reverse_strarr[i]) +'' + by_length.numbers_list[reverse_strarr[i]-1])
        else:
            return_list.append(str(reverse_strarr[i]))
    return return_list

