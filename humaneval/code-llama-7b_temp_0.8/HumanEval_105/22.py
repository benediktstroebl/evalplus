
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

    # First, check that the array is not empty.
    if len(arr) == 0:
        return []
    # Second, check that all elements in the array are integers in the range 1 to 9.
    for elem in arr:
        if not isinstance(elem, int) or elem < 1 or elem > 9:
            raise ValueError("Non integer or out of range.")
    # Third, check that all elements in the array are integers in the range 1 to 9.
    # If not, raise an error.
    for elem in arr:
        if not isinstance(elem, int) or elem < 1 or elem > 9:
            raise ValueError("Non integer or out of range.")
    # Fourth, sort the elements in the array.
    arr.sort()
    # Fifth, reverse the order of the elements in the array.
    arr.reverse()
    # Sixth, reverse the names of the elements in the array.
    rev_names = []
    for elem in arr:
        rev_names.append(reverse_num_to_name(elem))

    return rev_names
