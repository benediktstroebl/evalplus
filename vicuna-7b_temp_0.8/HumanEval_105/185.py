
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
    # This code is only checking whether the input array is not empty and
    # all the elements are in the range of 1 to 9
    if len(arr) > 0 and all(elem >= 1 and elem <= 9 for elem in arr):
        result = []
        start = 0
        end = 0
        while start < len(arr) and end < len(arr):
            if arr[start] < 10:
                result.append(str(arr[start]))
                start += 1
            elif arr[end] < 10:
                result.append(str(arr[end]))
                end += 1
            else:
                result.append(arr[start])
                start = end
                end = start
        return result
    else:
        return []
