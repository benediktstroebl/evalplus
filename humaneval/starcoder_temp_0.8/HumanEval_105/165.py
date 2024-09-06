
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
    
    rev = sorted([num for num in arr if 1<=num<=9], reverse=True)
    
    for i, val in enumerate(rev):
        if val == 1:
            rev[i] = 'One'
        elif val == 2:
            rev[i] = 'Two'
        elif val == 3:
            rev[i] = 'Three'
        elif val == 4:
            rev[i] = 'Four'
        elif val == 5:
            rev[i] = 'Five'
        elif val == 6:
            rev[i] = 'Six'
        elif val == 7:
            rev[i] = 'Seven'
        elif val == 8:
            rev[i] = 'Eight'
        elif val == 9:
            rev[i] = 'Nine'
        
    return rev
