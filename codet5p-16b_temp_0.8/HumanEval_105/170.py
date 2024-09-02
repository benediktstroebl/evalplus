
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

    
    
    def check_length(x):
        for i in range(len(str(x))):
            if str(x)[i] not in "123456789":
                return False
        return True
    
    def reverse_array(x):
        return x[::-1]
    
    if len(arr) == 0:
        return []
    elif check_length(arr[0]) is False:
        return []
    else:
        pass
        
    if len(arr) == 1:
        if check_length(arr[0]) is True:
            return []
        else:
            return ["One"]
    else:
        pass
    
    new_arr = [x for x in arr if x <= 9]
    new_arr = [x for x in new_arr if x >= 1]
    
    if len(new_arr) == 0:
        return []
    else:
        new_arr = reverse_array(new_arr)
        new_arr = [int(x) for x in new_arr]
        new_
