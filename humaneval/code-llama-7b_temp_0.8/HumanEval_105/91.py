
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
    # We want to sort the numbers in the range [1,9] and reverse them, so we will sort the original list and 
    # then reverse the sorted list. To reverse the sorted list, we can use the reverse() method.
    # 1) First, we want to sort the numbers in the array that are within the range [1, 9]. Since there are 9 
    # integers to consider, we can use the sorted() function with a key. 
    # 2) Next, we want to reverse the sorted list, so we can use the reverse() function.
    # 3) The last step is to replace each integer with its corresponding name. For this, we can use a dictionary.
    # 4) Finally, we can use the map() function to map each name to the list.

    return list(map(str, sorted(arr, reverse=True, key=lambda x: (9 - x) if x in range(1, 10) else x)))

