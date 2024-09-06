
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
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][sorted(arr)[::-1]]

assert by_length([]) == []
assert by_length([1]) == ['One']
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([7,1,3,5]) == ['Three', 'One', 'One']
assert by_length([3,4,5,6,7,8,9]) == ['Eight', 'Nine', 'Nine', 'Eight', 'Eight', 'Eight', 'Eight']
assert by_length([2,1,3]) == ['One', 'One', 'Two']
assert by_length([2,1,1,4,5,8,2,3]) == ['Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One', 'One', 'One']
assert by_length([1,2,3,4,5,6,7,8]) == ['One', 'One', 'One', 'One', 'One', 'One', 'One', 'One', 'One']
assert by_length([1,2,3,4,5,6,7,8,9]) == ['One', 'One', 'One', 'One', 'One', 'One', 'One', 'One', 'One']
assert by_length([8,3,5,4,2,1,6,7]) == ['Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight']



