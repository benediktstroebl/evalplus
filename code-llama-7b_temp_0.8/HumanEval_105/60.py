
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
    if arr.count(1) > 1:
        arr[arr.index(1)] = "One"
        arr[arr.index(1, 1)] = "One"
    elif arr.count(1) == 1:
        arr[arr.index(1)] = "One"
    elif arr.count(2) > 1:
        arr[arr.index(2)] = "Two"
        arr[arr.index(2, 1)] = "Two"
    elif arr.count(2) == 1:
        arr[arr.index(2)] = "Two"
    elif arr.count(3) > 1:
        arr[arr.index(3)] = "Three"
        arr[arr.index(3, 1)] = "Three"
    elif arr.count(3) == 1:
        arr[arr.index(3)] = "Three"
    elif arr.count(4) > 1:
        arr[arr.index(4)] = "Four"
        arr[arr.index(4, 1)] = "Four"
    elif arr.count(4) == 1:
        arr[arr.index(4)] = "Four"
    elif arr.count(5) > 1:
        arr[arr.index(5)] = "Five"
        arr[arr.index(5, 1)] = "Five"
    elif arr.count(5) == 1:
        arr[arr.index(5)] = "Five"
    elif arr.count(6) > 1:
        arr[arr.index(6)] = "Six"
        arr[arr.index(6, 1)] = "Six"
    elif arr.count(6) == 1:
        arr[arr.index(6)] = "Six"
    elif arr.count(7) > 1:
        arr[arr.index(7)] = "Seven"
        arr[arr.index(7, 1)] = "Seven"
    elif arr.count(7) == 1:
        arr[arr.index(
