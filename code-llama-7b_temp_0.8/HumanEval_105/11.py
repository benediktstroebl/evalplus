
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
    arr.sort()
    arr.reverse()
    
    array_to_return = []
    for n in arr:
        if n > 0 and n < 10:
            if n == 1:
                array_to_return.append("One")
            elif n == 2:
                array_to_return.append("Two")
            elif n == 3:
                array_to_return.append("Three")
            elif n == 4:
                array_to_return.append("Four")
            elif n == 5:
                array_to_return.append("Five")
            elif n == 6:
                array_to_return.append("Six")
            elif n == 7:
                array_to_return.append("Seven")
            elif n == 8:
                array_to_return.append("Eight")
            elif n == 9:
                array_to_return.append("Nine")

    return array_to_return

