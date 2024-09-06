
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
    # initialize result array to return
    result = []
    
    # sort the array
    arr.sort()
    
    # reverse the array
    arr.reverse()
    
    # for every value in the array
    for value in arr:
        # if value is in range 1-9, append the digit's name to result
        if 1 <= value <= 9:
            result.append(str(value))
    
    # for every value in the result array
    for index, value in enumerate(result):
        # replace the number string with its name
        result[index] = value.replace(value, name(int(value)))
    
    # return result array
    return result
