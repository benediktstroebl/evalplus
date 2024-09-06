
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

    # Setup an empty list
    new_arr = []
    # If the array is not empty
    if len(arr) > 0:
        # Sort the array by length, descending order
        arr = sorted(arr, key = len, reverse = True)
        # Iterate through the array
        for item in arr:
            # If the length is 1 or 2, convert it to the corresponding name
            if len(str(item)) == 1 or len(str(item)) == 2:
                if item == 1:
                    new_arr.append("One")
                elif item == 2:
                    new_arr.append("Two")
                elif item == 3:
                    new_arr.append("Three")
                elif item == 4:
                    new_arr.append("Four")
                elif item == 5:
                    new_arr.append("Five")
                elif item == 6:
                    new_arr.append("Six")
                elif item == 7:
                    new_arr.append("Seven")
                elif item == 8:
                    new_arr.append("Eight")
                elif item == 9:
                    new_arr.append("Nine")
            # If the length is not 1 or 2, ignore it
            else:
                continue
    # If the array is empty, return an empty array
    else:
        return []
    # Reverse the array and return it
    new_arr.reverse()
    return new_arr
