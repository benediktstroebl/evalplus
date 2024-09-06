
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

    # # 1. Use the built-in sort() method
    # arr.sort()
    #
    # # 2. Use the lambda function
    # arr = [lambda x: x if x in (1, 2, 3, 4, 5, 6, 7, 8, 9) else 0 for x in arr]
    # arr = sorted(arr)
    # arr = [str(x) for x in arr if x > 0]

    # 3. Use the reduce() method
    arr = reduce(lambda x, y: x if x in (1, 2, 3, 4, 5, 6, 7, 8, 9) else y, arr)
    arr = sorted(arr)
    arr = [str(x) for x in arr if x > 0]

    # 4. Use the lambda function with sort()
    arr = [lambda x: x if x in (1, 2, 3, 4, 5, 
