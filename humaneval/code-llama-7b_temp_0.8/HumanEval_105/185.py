
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
    # RW
    # Hint: Use `sorted` to sort the array
    # Hint: Use `list[::-1]` to reverse the array
    # Hint: Use the `str` built-in class to convert numbers into strings
    # Hint: Use the `dict` built-in class to map strings to numbers
    # Hint: Use `str.isdigit()` to check if a string is a number
    # Hint: Use `dict.get(key, default_value)` to check if a key is present, and if not, return a default value
    # Hint: Use `isinstance(object, type)` to check if an object is an instance of a type
    # RW
    # RW
    return []
    # RW
    # RW
