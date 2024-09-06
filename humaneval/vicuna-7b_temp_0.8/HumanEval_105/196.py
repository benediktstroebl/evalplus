
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
    # Empty array return empty list
    if not arr:
        return []
    
    # Handle the case when the array has only one element
    if len(arr) == 1:
        return [arr[0]]
    
    # Get the length of the array
    n = len(arr)
    
    # Initialize the result to store the names
    result = [arr[i] for i in range(n)]
    
    # Create a copy of the original array for the sorting
    arr_copy = arr.copy()
    
    # Sort the array
    arr_copy.sort()
    
    # Reverse the array
    arr_copy.reverse()
    
    # Replace each number with its name
    for i in range(n):
        result[i] = names.index(arr_copy[i])
    
    return result
