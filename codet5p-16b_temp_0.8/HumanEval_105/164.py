
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

    
    return_arr = []
    
    if len(arr) == 0:
        return return_arr
    
    if len(arr) >= 1:
        arr.sort()
        arr.reverse()
        for x in arr:
            if x > 9:
                continue
            elif x < 1:
                continue
            elif x >= 1 and x <= 9:
                return_arr.append("One")
                return_arr.append("Two")
                return_arr.append("Three")
                return_arr.append("Four")
                return_arr.append("Five")
                return_arr.append("Six")
                return_arr.append("Seven")
                return_arr.append("Eight")
                return_arr.append("Nine")
                return return_arr
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
