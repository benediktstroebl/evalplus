
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

    
    """
    We can break this into two smaller problems:
        1. Sort the array of numbers that are between 1 and 9 inclusive
        2. Reverse the resulting array
    """
    
    if len(arr) == 0:
        return arr
    
    num_list = []
    for i in arr:
        if 1 <= i <= 9:
            num_list.append(i)
    
    num_list.sort()
    num_list.reverse()
    
    new_list = []
    for i in num_list:
        if i == 1:
            new_list.append("One")
        elif i == 2:
            new_list.append("Two")
        elif i == 3:
            new_list.append("Three")
        elif i == 4:
            new_list.append("Four")
        elif i == 5:
            new_list.append("Five")
        elif i == 6:
            new_list.append("Six")
        elif i == 7:
            new_list.append("Seven")
        
