
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
    # Your code goes below this line
    arr = []
    if len(arr) == 0:
        return arr
    arr.append(str(1))
    arr.append(str(2))
    arr.append(str(3))
    arr.append(str(4))
    arr.append(str(5))
    arr.append(str(6))
    arr.append(str(7))
    arr.append(str(8))
    arr.append(str(9))
    arr.append(str(10))
    if arr[0] == str(1):
        arr.append("One")
    if arr[1] == str(2):
        arr.append("Two")
    if arr[2] == str(3):
        arr.append("Three")
    if arr[3] == str(4):
        arr.append("Four")
    if arr[4] == str(5):
        arr.append("Five")
    if arr[5] == str(6):
        arr.append("Six")
    if arr
