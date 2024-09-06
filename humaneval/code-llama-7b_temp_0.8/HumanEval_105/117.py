
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
    import string
    import re
    
    # Check if the array is empty or has numbers that are not between 1 and 9 inclusive
    if len(arr) == 0 or any([not re.match(r'^[1-9]$', str(x)) for x in arr]):
        return []
    
    # Get the string representations of the integers between 1 and 9
    integer_strings = []
    for i in range(1, 10):
        integer_strings.append(string.ascii_lowercase[i-1])
    
    # Reverse the input array and sort it
    arr.reverse()
    arr.sort()
    
    # Return the string representations of the integers in the input array
    result = []
    for i in range(len(arr)):
        if arr[i] in range(1, 10):
            result.append(integer_strings[arr[i]-1])
    return result
    

