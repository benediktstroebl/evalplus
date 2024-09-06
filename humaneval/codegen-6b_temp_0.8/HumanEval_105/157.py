
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
    
    arr = sorted([i for i in arr if 1 <= i <= 9])
    arr = arr[::-1]
    
    shift = 0
    ans = []
    for i, n in enumerate(arr):
        shift += n * (10 ** i)
        ans.append(str(n))
    
    return ans



assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([2, -1, 55]) == ['One']
assert by_length([1, 1, 2]) == ['One', 'One']
assert by_length([1, 2, 3]) == ['One', 'Two', 'Three']
assert by_length([9, 1]) == ['Nine', 'One']
assert by_length([9, 1, 0]) == ['Nine', 'One', 'Zero']
assert by_length([0]) == ['Zero']














































