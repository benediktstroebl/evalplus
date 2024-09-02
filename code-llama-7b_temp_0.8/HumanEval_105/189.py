
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
    # 1st case:
    # The array is empty
    if not arr:
        return []
    
    # 2nd case:
    # The array has only one number
    if len(arr) == 1:
        num = arr[0]
        if 1 <= num <= 9:
            return [convert(num)]
        else:
            return []
    
    # 3rd case:
    # The array has two or more numbers
    res = []
    if len(arr) > 1:
        arr.sort()
        for elm in arr[::-1]:
            if 1 <= elm <= 9:
                res.append(convert(elm))
    return res
