
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
    # your code here

    # test case: empty array
    if not arr:
        return []

    # test case: has strange numbers
    new_arr = []
    for num in arr:
        if 1 <= num <= 9:
            new_arr.append(num)
    arr = new_arr
    if not arr:
        return []

    # sort 1, 2, ..., 9
    order = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    d = dict(zip(nums, order))
    arr.sort()
    arr.reverse()
    return [d[num] for num in arr]

