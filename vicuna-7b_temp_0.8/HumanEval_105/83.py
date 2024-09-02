
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
    from math import log2
    
    arr = list(arr)
    while arr:
        # find the length of the current longest block
        current_len = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]*2:
                current_len += 1
        longest_block = arr[:current_len]
        
        # swap the current block with the last block
        arr[current_len-1::-1] = longest_block
        
        # remove the current block
        del arr[current_len::]
    
    return arr
