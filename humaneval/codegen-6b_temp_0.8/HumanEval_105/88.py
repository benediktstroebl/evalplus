
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
    arr.sort()
    arr.reverse()
    for i in range(len(arr)):
        if arr[i] < 1 or arr[i] > 9:
            arr[i] = None
    arr = [x for x in arr if x]
    for i in range(len(arr)):
        if arr[i] == 'One':
            arr[i] = '1'
        elif arr[i] == 'Two':
            arr[i] = '2'
        elif arr[i] == 'Three':
            arr[i] = '3'
        elif arr[i] == 'Four':
            arr[i] = '4'
        elif arr[i] == 'Five':
            arr[i] = '5'
        elif arr[i] == 'Six':
            arr[i] = '6'
        elif arr[i] == 'Seven':
            arr[i] = '7'
        elif arr[i] == 'Eight':
            arr[i] = '8'
        elif arr[i] == 'Nine':
            arr[i] = '9'
    return arr

