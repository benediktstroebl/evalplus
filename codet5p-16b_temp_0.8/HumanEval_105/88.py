
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
    if len(arr) == 1:
        if arr[0] == 1:
            return ["One"]
        elif arr[0] == 2:
            return ["Two"]
        elif arr[0] == 3:
            return ["Three"]
        elif arr[0] == 4:
            return ["Four"]
        elif arr[0] == 5:
            return ["Five"]
        elif arr[0] == 6:
            return ["Six"]
        elif arr[0] == 7:
            return ["Seven"]
        elif arr[0] == 8:
            return ["Eight"]
        elif arr[0] == 9:
            return ["Nine"]
    
    small = [i for i in range(1, 10)]
    for i in range(len(arr)):
        if arr[i] < 1 or arr[i] > 9:
            arr[i] = " "
    small.sort()
    small.reverse()
    for i in range(len(arr)):
        
