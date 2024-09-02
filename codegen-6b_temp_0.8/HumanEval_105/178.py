
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
    if len(arr) == 0:
        return []
    arr = sorted([x for x in arr if x >= 0 and x <= 9])
    return [_get_name(x) for x in arr[::-1]]


assert by_length([0, 0, 0]) == []
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['One', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'Nine']
assert by_length([1, 2, 2, 2]) == ['One', 'Two', 'Two', 'Two']


"""
If you are not sure how to solve this problem on your own, please solve it using the shorter solution.
"""
