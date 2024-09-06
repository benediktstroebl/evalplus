
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
    return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]


assert(by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["One", "One", "Two", "Two", "Three", "Four", "Five", "Eight", "Nine"])
assert(by_length([]) == [])
assert(by_length([1, -1 , 55]) == ["One", "One", "Two", "Two", "Three", "Five", "55"])
assert(by_length([2]) == ["Two"])
assert(by_length([3, 300, 2, 1]) == ["One", "Three", "Three", "Two"])
assert(by_length([-3, 4, 1, -1, -4, -6, -99, 23]) == ["One", "One", "Two", "Two", "Three", "Three", "Four", "Four", "Five"])
assert(by_length([12, 123, 34, 67, 9, -67, -13, -123, -123]) == ["One", "One", "Two", "Two", "Three", "Two", "Three", "Three", "Four"])
assert(by_length([10, 1, 4, 6, 1, -1, -99, 23, 100]) == ["One", "One", "Two", "Two", "Three", "Three", "Four", "Four", "Five"])
assert(by_length([8, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])
assert(by_length([5, 1, -1, -4, -6, -99, 23, 100]) == ["Five", "One", "One", "Two", "Two", "Three", "Three", "Four", "Four", "Five"])
assert(by_length([5, 6, 4, 1, 6, 4, 5, 2, 1]) == ["Five", "Five", "Four", "Four", "Three", "Three", "Two", "Two", "One", "One"])
assert(