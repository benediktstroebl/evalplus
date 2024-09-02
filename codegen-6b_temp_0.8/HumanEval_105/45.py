
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
    
    def by_length_helper(arr, reverse):
        if not arr:
            return []

        n = len(arr)
        if n < 2:
            return [str(arr[0])]
        
        if n < 3:
            return [str(arr[0] + 1), str(arr[0])]
        
        if n < 4:
            return [str(arr[0] + 1), str(arr[0]), str(arr[0] + 2)]
        
        if n < 5:
            return [str(arr[0] + 1), str(arr[0]), str(arr[0] + 2), str(arr[0] + 1)]
        
        if n < 8:
            return [str(arr[0] + 1), str(arr[0]), str(arr[0] + 2), str(arr[0] + 1),
                    str(arr[0] + 1), str(arr[0] + 1), str(arr[0] + 3), str(arr[0] + 2)]
        
        if n < 10:
            return [str(arr[0] + 1), str(arr[0]), str(arr[0] + 2), str(arr[0] + 1),
                    str(arr[0] + 1), str(arr[0] + 1), str(arr[0] + 3), str(arr[0] + 2),
                    str(arr[0] + 1), str(arr[0] + 1), str(arr[0] + 4), str(arr[0] + 3)]
        
        if n < 15:
            return [str(arr[0] + 1), str(arr[0]), str(arr[0] + 2), str(arr[0] + 1),
                    str(arr[0] + 1), str(arr[0] + 1), str(arr[0] + 3), str(arr[0] + 2),
                    str(arr[0] + 1), str(arr[0] + 1), str(arr[0] + 4), str(arr[0] + 3),
                    str(arr[0] + 1), str(arr[0] + 1), str