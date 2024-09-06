
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
    #first, make sure the array is empty or contains only integers between 1 and 9
    for num in arr:
        if num < 1 or num > 9:
            return []
    #now, we need to sort the array
    arr.sort()
    #now, reverse it!
    arr.reverse()
    #now, put the numbers back to their names
    names = []
    for num in arr:
        if num == 1:
            names.append("One")
        elif num == 2:
            names.append("Two")
        elif num == 3:
            names.append("Three")
        elif num == 4:
            names.append("Four")
        elif num == 5:
            names.append("Five")
        elif num == 6:
            names.append("Six")
        elif num == 7:
            names.append("Seven")
        elif num == 8:
            names.append("Eight")
        elif num == 9:
            names.append("Nine")
    return names

