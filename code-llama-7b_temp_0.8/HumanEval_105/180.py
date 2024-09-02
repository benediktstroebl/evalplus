
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
    # Write your code here.
    # 2 -> one
    # 1 -> one
    # 5 -> five
    # 8 -> eight
    # 2 -> two
    # 3 -> three
    # 1 -> one
    return [
        "One" if digit == 1 else "Two" if digit == 2 else "Three"
        if digit == 3 else "Four" if digit == 4 else "Five"
        if digit == 5 else "Six" if digit == 6 else "Seven"
        if digit == 7 else "Eight" if digit == 8 else "Nine"
        for digit in sorted(arr, reverse=True)
        if 1 <= digit <= 9
    ]

