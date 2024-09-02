
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
        return []
    arr = [i for i in arr if i >= 1 and i <= 9]
    arr.sort()
    arr.reverse()
    arr = [str(i) for i in arr]
    arr = [
        "One" if str(i) == "1" else
        "Two" if str(i) == "2" else
        "Three" if str(i) == "3" else
        "Four" if str(i) == "4" else
        "Five" if str(i) == "5" else
        "Six" if str(i) == "6" else
        "Seven" if str(i) == "7" else
        "Eight" if str(i) == "8" else
        "Nine" if str(i) == "9" else
        None
        for i in arr
    ]
    return arr
