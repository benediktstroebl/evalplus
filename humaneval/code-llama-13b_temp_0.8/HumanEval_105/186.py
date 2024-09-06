
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
    result = []
    for e in arr:
      if e >= 1 and e <= 9:
        result.append(str(e))
    
    result.sort()
    result.reverse()
    result = [x.replace('1', 'One') for x in result]
    result = [x.replace('2', 'Two') for x in result]
    result = [x.replace('3', 'Three') for x in result]
    result = [x.replace('4', 'Four') for x in result]
    result = [x.replace('5', 'Five') for x in result]
    result = [x.replace('6', 'Six') for x in result]
    result = [x.replace('7', 'Seven') for x in result]
    result = [x.replace('8', 'Eight') for x in result]
    result = [x.replace('9', 'Nine') for x in result]
    
    return result

