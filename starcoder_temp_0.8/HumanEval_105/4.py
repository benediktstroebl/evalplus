
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
    new_arr = []
    for num in arr:
        if num >= 1 and num <= 9:
            new_arr.append(num)
    new_arr.sort()
    new_arr.reverse()
    new_arr2 = []
    for num in new_arr:
        if num == 1:
            new_arr2.append('One')
        elif num == 2:
            new_arr2.append('Two')
        elif num == 3:
            new_arr2.append('Three')
        elif num == 4:
            new_arr2.append('Four')
        elif num == 5:
            new_arr2.append('Five')
        elif num == 6:
            new_arr2.append('Six')
        elif num == 7:
            new_arr2.append('Seven')
        elif num == 8:
            new_arr2.append('Eight')
        elif num == 9:
            new_arr2.append('Nine')
    return new_arr2
