
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
    # by inspection the order of the array is given by the order of the digit
    # in the number. So the question then becomes how do we extract the digits
    # from the array and sort them in that order.
    # sorted() can sort a list of strings by their first character and then their second
    # character. So we can use this to our advantage to sort the array of numbers
    # as they are ordered in the string representation of the number
    return [
        "One" if n == 1 else
        "Two" if n == 2 else
        "Three" if n == 3 else
        "Four" if n == 4 else
        "Five" if n == 5 else
        "Six" if n == 6 else
        "Seven" if n == 7 else
        "Eight" if n == 8 else
        "Nine" if n == 9 else
        None
        for n in sorted(arr)
    ]

