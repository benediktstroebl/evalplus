
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
    lst = []
    for num in arr:
        if num > 0 and num < 10:
            lst.append(num)
    lst.sort(reverse = True)
    for num in lst:
        if num == 1:
            lst[lst.index(num)] = "One"
        elif num == 2:
            lst[lst.index(num)] = "Two"
        elif num == 3:
            lst[lst.index(num)] = "Three"
        elif num == 4:
            lst[lst.index(num)] = "Four"
        elif num == 5:
            lst[lst.index(num)] = "Five"
        elif num == 6:
            lst[lst.index(num)] = "Six"
        elif num == 7:
            lst[lst.index(num)] = "Seven"
        elif num == 8:
            lst[lst.index(num)] = "Eight"
        elif num == 9:
            lst[lst.index(num)] = "Nine"
    return lst
    
    
