
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

    arr = [i for i in arr if 1 <= i <= 9] # ignore any number not in the range 1-9

    # sorting
    arr = sorted(arr, key=lambda i: (i % 2, i // 2))
    arr = sorted(arr, reverse=True)

    # if array is empty
    if not arr:
        return []

    # reverse and find the corresponding name
    arr = [str(i) for i in arr]
    result = [convert_number_to_name(i) for i in arr]

    return result

