
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
    
    def digit_to_name(digit):
        if digit == 1:
            return "One"
        if digit == 2:
            return "Two"
        if digit == 3:
            return "Three"
        if digit == 4:
            return "Four"
        if digit == 5:
            return "Five"
        if digit == 6:
            return "Six"
        if digit == 7:
            return "Seven"
        if digit == 8:
            return "Eight"
        if digit == 9:
            return "Nine"
        return str(digit)
        
    return [digit_to_name(num) for num in arr]

