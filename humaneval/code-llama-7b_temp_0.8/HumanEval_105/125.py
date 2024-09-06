
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
    
    # Sort the numbers in the array
    arr.sort()
    
    # Remove all numbers that are not between 1 and 9
    while 1 in arr:
        arr.remove(1)
    while 2 in arr:
        arr.remove(2)
    while 3 in arr:
        arr.remove(3)
    while 4 in arr:
        arr.remove(4)
    while 5 in arr:
        arr.remove(5)
    while 6 in arr:
        arr.remove(6)
    while 7 in arr:
        arr.remove(7)
    while 8 in arr:
        arr.remove(8)
    while 9 in arr:
        arr.remove(9)
    
    # Reverse the array and replace the numbers with the name of the number
    arr.reverse()
    for i, num in enumerate(arr):
        if num == 1:
            arr[i] = "One"
        elif num == 2:
            arr[i] = "Two"
        elif num == 3:
            arr[i] = "Three"
        elif num == 4:
            arr[i] = "Four"
        elif num == 5:
            arr[i] = "Five"
        elif num == 6:
            arr[i] = "Six"
        elif num == 7:
            arr[i] = "Seven"
        elif num == 8:
            arr[i] = "Eight"
        elif num == 9:
            arr[i] = "Nine"
    
    return arr
