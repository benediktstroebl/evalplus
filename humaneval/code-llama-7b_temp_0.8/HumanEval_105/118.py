
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
    # take out the numbers between 1 and 9 inclusive and reverse the order
    arr_sorted = sorted(arr, reverse=True)[0:9]
    
    # turn the sorted array into a string to access the corresponding string names
    arr_string = "".join(str(n) for n in arr_sorted)
    
    # create a list of string names in the order of the sorted array
    names = []
    for i in arr_string:
        names.append("One" if i == 1 else
                     "Two" if i == 2 else
                     "Three" if i == 3 else
                     "Four" if i == 4 else
                     "Five" if i == 5 else
                     "Six" if i == 6 else
                     "Seven" if i == 7 else
                     "Eight" if i == 8 else
                     "Nine")
    
    return names

