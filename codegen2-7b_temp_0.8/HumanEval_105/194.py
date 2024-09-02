
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
    arr = [int(i) for i in arr]
    arr = sorted(arr)
    arr = list(reversed(arr))
    for i, num in enumerate(arr):
        if num < 10:
            arr[i] = str(num)
        elif num == 10:
            arr[i] = "One"
        elif num == 11:
            arr[i] = "Two"
        elif num == 12:
            arr[i] = "Three"
        elif num == 13:
            arr[i] = "Four"
        elif num == 14:
            arr[i] = "Five"
        elif num == 15:
            arr[i] = "Six"
        elif num == 16:
            arr[i] = "Seven"
        elif num == 17:
            arr[i] = "Eight"
        elif num == 18:
            arr[i] = "Nine"
    return arr
