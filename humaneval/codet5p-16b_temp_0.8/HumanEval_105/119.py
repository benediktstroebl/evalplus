
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

    
    # sort the array based on its length, reversed
    sorted_arr = sorted(arr, key=len, reverse=True)
    
    # filter out only the numbers that are between 1 and 9 inclusive
    filtered_arr = [i for i in sorted_arr if 1 <= int(i) <= 9]

    # reverse the filtered array
    reversed_arr = filtered_arr[::-1]

    # replace the numbers with corresponding numbers
    final_arr = [str(i) for i in reversed_arr]
    
    return ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
  
  
