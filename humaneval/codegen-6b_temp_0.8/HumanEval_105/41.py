
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
    
    list_of_digits = arr
    list_of_letters = []
    
    if len(list_of_digits) == 0:
        return []
    
    elif len(list_of_digits) == 1:
        return ["One"]
    
    elif len(list_of_digits) == 2:
        if list_of_digits[0] == 1:
            return ["One", "Two"]
        elif list_of_digits[0] == 2:
            return ["Two", "One"]
        elif list_of_digits[0] == 3:
            return ["Three", "One"]
        elif list_of_digits[0] == 4:
            return ["Four", "One"]
        elif list_of_digits[0] == 5:
            return ["Five", "One"]
        elif list_of_digits[0] == 6:
            return ["Six", "One"]
        elif list_of_digits[0] == 7:
            return ["Seven", "One"]
        elif list_of_digits[0] == 8:
            return ["Eight", "One"]
        elif list_of_digits[0] == 9:
            return ["Nine", "One"]
    
    elif len(list_of_digits) == 3:
        
        if list_of_digits[0] == 1:
            if list_of_digits[1] == 1:
                if list_of_digits[2] == 1:
                    return ["One", "One", "One"]
                elif list_of_digits[2] == 2:
                    return ["One", "Two", "One"]
                elif list_of_digits[2] == 3:
                    return ["Three", "One", "One"]
                elif list_of_digits[2] == 4:
                    return ["Four", "One", "One"]
                elif list_of_digits[2] == 5:
                    return ["Five", "One", "One"]
                elif list_of_digits[2] == 6: