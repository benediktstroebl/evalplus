
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
    if not arr:
        return []
    
    sorted_arr = sorted(arr)
    
    should_reverse = True
    for a in sorted_arr:
        if a in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            should_reverse = False
            break
    
    if should_reverse:
        reverse(sorted_arr, 0, len(sorted_arr) - 1)
        return [digit_name[digit] for digit in sorted_arr]
    else:
        return [digit_name[digit] for digit in reversed(sorted_arr)]
