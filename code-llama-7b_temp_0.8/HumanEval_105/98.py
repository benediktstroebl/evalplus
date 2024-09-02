
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
    result = []
    
    # Check if array is empty
    if arr:
        # Create array that contains length of each item in arr
        length = [len(str(i)) for i in arr]
        
        # Sort the length array and reverse it
        length.sort()
        length.reverse()
        
        # Add the corresponding names to result
        for x in length:
            for y in arr:
                if len(str(y)) == x:
                    result.append(str(y))
                    arr.remove(y)
    
    return [translate(x) for x in result]

