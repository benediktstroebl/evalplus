
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
    ret = []
    if arr:
      arr = sorted(set(arr) & set([x for x in range(1, 10)]))
      for i in arr:
        if i == 9:
          ret.append('Nine')
        elif i == 8:
          ret.append('Eight')
        elif i == 7:
          ret.append('Seven')
        elif i == 6:
          ret.append('Six')
        elif i == 5:
          ret.append('Five')
        elif i == 4:
          ret.append('Four')
        elif i == 3:
          ret.append('Three')
        elif i == 2:
          ret.append('Two')
        elif i == 1:
          ret.append('One')
        elif i == 0:
          ret.append('Zero')
        else:
          return None
      return ret[::-1]
    else:
      return None
