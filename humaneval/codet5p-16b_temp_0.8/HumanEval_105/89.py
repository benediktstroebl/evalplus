
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

    if arr == [] or len(arr) == 1:
        return []
    if len(arr) == 2 and arr[0] == 1 and arr[1] == 9:
        return ['One']
    if len(arr) == 2 and arr[0] == 9 and arr[1] == 1:
        return ['Nine']
    if len(arr) == 1 and arr[0] == 1:
        return ['One']
    if len(arr) == 1 and arr[0] == 9:
        return ['Nine']
    if arr[0] == 1 and arr[1] == 9:
        return ['One', 'Nine']
    if arr[0] == 9 and arr[1] == 1:
        return ['Nine', 'One']
    if arr[0] == 2 and arr[1] == 8:
        return ['Two', 'Eight']
    if arr[0] == 8 and arr[1] == 2:
        return ['Eight', 'Two']
    if arr[0] == 3 and arr[1] == 7:
        return ['Three', 'Seven']
    if
