
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
    
    def get_name(i):
        if i == 1:
            return "One"
        elif i == 2:
            return "Two"
        elif i == 3:
            return "Three"
        elif i == 4:
            return "Four"
        elif i == 5:
            return "Five"
        elif i == 6:
            return "Six"
        elif i == 7:
            return "Seven"
        elif i == 8:
            return "Eight"
        elif i == 9:
            return "Nine"

    ret = []
    for i in reversed(sorted(arr)):
        if i in range(1, 10):
            ret.append(get_name(i))
        else:
            ret.append(str(i))
    return ret
