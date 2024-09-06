
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
    result = []
    for integer in arr:
        if 1 <= integer <= 9:
            result.append(DIGITS[integer - 1])
        else:
            result.append(integer)
    return result[::-1]
    
assert by_length([]) == []
assert by_length([1, 8, 5, 3]) == ['Five', 'Eight', 'Three', 'One']
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One', 'Eight']
assert by_length([9, 9, 9]) == ['Nine', 'Nine', 'Nine']
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == ['One', 'One', 'One', 'Eight', 'Eight', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'Zero']




