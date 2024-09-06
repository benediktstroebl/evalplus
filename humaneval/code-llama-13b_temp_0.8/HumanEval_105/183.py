
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
    #your code here
    #Note: you can't change the original array
    #       and the return value has to be a list
    
    output = []
    if not arr:
        return output
    
    temp_arr = []
    for item in arr:
        if item > 0 and item <= 9:
            temp_arr.append(item)
    temp_arr = sorted(temp_arr, reverse=True)
    
    for item in temp_arr:
        if item == 1:
            output.append('One')
        elif item == 2:
            output.append('Two')
        elif item == 3:
            output.append('Three')
        elif item == 4:
            output.append('Four')
        elif item == 5:
            output.append('Five')
        elif item == 6:
            output.append('Six')
        elif item == 7:
            output.append('Seven')
        elif item == 8:
            output.append('Eight')
        elif item == 9:
            output.append('Nine')
    return output

