
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
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return ['One']
    else:
        temp = []
        for i in arr:
            if i < 10:
                temp.append(i)
            else:
                if i == 1:
                    temp.append('One')
                elif i == 2:
                    temp.append('Two')
                elif i == 3:
                    temp.append('Three')
                elif i == 4:
                    temp.append('Four')
                elif i == 5:
                    temp.append('Five')
                elif i == 6:
                    temp.append('Six')
                elif i == 7:
                    temp.append('Seven')
                elif i == 8:
                    temp.append('Eight')
                elif i == 9:
                    temp.append('Nine')
        return temp
