
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
    num_to_name = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                   7: 'Seven', 8: 'Eight', 9: 'Nine'}
    if len(arr) == 0:
        return []
    length = len(arr)
    l = 0
    r = length - 1
    while l < r:
        while arr[l] < 1 or arr[l] > 9:
            l += 1
        while arr[r] < 1 or arr[r] > 9:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return [num_to_name[i] for i in arr[::-1]]

