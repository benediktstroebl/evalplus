
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
    output = []
    for i in arr:
        if i in range(1, 10):
            output.append(i)
    output.sort(reverse = True)
    fibs = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    for x in output:
        fibs.pop(x)
    output.extend(fibs)
    return output

assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8]) == ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
assert by_length([]) == []
assert by_length([5, 1, 5, 3, 2, 3, 2, 4, 4]) == ["Four", "One", "One", "Two", "Two", "Three", "Three", "Four", "Five"]
assert by_length([1]) == ["One"]
assert by_length([9, 9, 9]) == ["Nine"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine"]
assert by_length([1, 2, 0, 0, 0, 0]) == ["Zero"]
assert by_length([0]) == ["Zero"]
assert by_length([10, 1, 1, 9, 0, 0, 0, 0, 0]) == ["One", "One", "One", "Nine", "Zero", "Zero", "Zero", "Zero", "Zero"]
assert by_length([0, 0, 0]) == ["Zero"]
