
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

    
    arr = sorted(filter(lambda n: 1 <= n <= 9, arr))
    return [i for _, i in sorted(zip([i for i in range(1, 10)], map(lambda n: "Nine" if n == 9 else "Eight" if n == 8 else "Seven" if n == 7 else "Six" if n == 6 else "Five" if n == 5 else "Four" if n == 4 else "Three" if n == 3 else "Two" if n == 2 else "One", arr)), reverse=True)]
    
