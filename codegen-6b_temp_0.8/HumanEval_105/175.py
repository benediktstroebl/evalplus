
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
    
    array = arr[:]
    array.sort()
    array.reverse()
    output = []
    for num in array:
        if 1 <= num <= 9:
            output.append(numbers[num - 1])
    return output
    
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([1, -1 , 55]) == ['One']
assert by_length([0, -1, 2, 0, 3, 4, 5, 6, 7, 8, 9]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One', 'Nine', 'Six', 'Seven', 'Eight', 'Five', 'Four']
assert by_length([22, 22, 22, 22, 22, 22, 22, 22]) == ['Nine', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight', 'Eight']
assert by_length([99,11,22,33,44]) == ['Nine','Nine','Nine','Nine','Nine']
assert by_length([123, 456, 567, 890]) == ['One', 'Two', 'Three', 'Four']
assert by_length([897,9,9,9]) == ['Nine', 'Nine', 'Nine', 'Nine']
assert by_length([1, 1, 1, 1, 1, 1, 1]) == ['One', 'One', 'One', 'One', 'One', 'One', 'One']
assert by_length([1, 1, 1, 1, 1]) == ['One', 'One', 'One', 'One', 'One']

