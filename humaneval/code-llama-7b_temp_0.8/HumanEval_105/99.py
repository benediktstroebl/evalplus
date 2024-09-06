
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
    assert isinstance(arr, list), 'The argument must be an array'
    # assert 1 <= min(arr) <= 9, 'The list must contain numbers between 1 and 9'
    # assert 1 <= max(arr) <= 9, 'The list must contain numbers between 1 and 9'
    for i in arr:
        assert isinstance(i, int), 'The argument must be an array of integers'
        assert 1 <= i <= 9, 'The list must contain numbers between 1 and 9'

    # TODO
    return
