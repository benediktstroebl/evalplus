
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
    # base case
    if not arr:
        return []
    
    # find the middle index
    middle_index = len(arr) // 2
    
    # divide the array into two parts
    left = arr[:middle_index]
    right = arr[middle_index:]
    
    # handle the left part
    left_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    left_sorted = by_length(left)
    left_sorted = sorted(left_sorted)
    left_names_index = [left_names.index(x) for x in left_sorted]
    left_names_index = [len(str(x)) - 1 if x >= 10 else x - 1 for x in left_names_index]
    left_names_index = sorted(left_names_index)
    left = [x for x in left_names_index if x >= 0]
    left = [str(x) if x >= 10 else "0" + str(x) for x in left]
    left = "".join(left)
    
    # handle the right part
    right_names = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    right_sorted = by_length(right)
    right_sorted = sorted(right_sorted)
    right_names_index = [x - 1 for x in right_sorted]
    right_names_index = sorted(right_names_index)
    right_names_index = [str(x) if x >= 10 else "0" + str(x) for x in right_names_index]
    right_names_index = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    right = [x for x in right_names_index if x >= 0]
    right = "".join(right)
    
    # join the left and right parts
    result = left + right
    
    return result

arr = [1, 
