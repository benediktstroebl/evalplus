
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
    if not arr:
        return []
    
    numbers = sorted([i for i in arr if i > 0 and i <= 9])
    numbers = sorted(numbers, reverse=True)
    result = [x for x in map(str, numbers)]
    return result


assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Two", "Two", "Three", "Three", "One", "One", "Two", "One"]
assert by_length([1, -1 , 55]) == ['One']
assert by_length([]) == []
assert by_length([1, -1 , -55]) == ['One']
assert by_length([1, 1, 1, 4, 5, 8, 2, 3]) == ['One', 'One', 'Two', 'Two', 'Three', 'Three', 'Four', 'Five']
assert by_length([2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == ['Two', 'Two', 'Three', 'Three', 'Four', 'Four', 'Four', 'Four', 'Four', 'Four']

