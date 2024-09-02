
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
    
    
    if 1 not in arr:
        return arr
    
    else:
        num_arr = sorted(arr)
        num_arr = num_arr[::-1]
        num_arr = num_arr.replace(1,'One')
        num_arr = num_arr.replace(2,'Two')
        num_arr = num_arr.replace(3,'Three')
        num_arr = num_arr.replace(4,'Four')
        num_arr = num_arr.replace(5,'Five')
        num_arr = num_arr.replace(6,'Six')
        num_arr = num_arr.replace(7,'Seven')
        num_arr = num_arr.replace(8,'Eight')
        num_arr = num_arr.replace(9,'Nine')
        return
