
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
    # Define an output array for our sorted result
    result = []

    # Sort the array
    arr = sorted(arr)

    # Reverse the sorted array
    arr.reverse()

    # Loop through the sorted array and apply the necessary logic
    for num in arr:
        # If the number is between 1 and 9, add the associated string to the output array
        if 1 <= num <= 9:
            if num == 1:
                result.append("One")
            elif num == 2:
                result.append("Two")
            elif num == 3:
                result.append("Three")
            elif num == 4:
                result.append("Four")
            elif num == 5:
                result.append("Five")
            elif num == 6:
                result.append("Six")
            elif num == 7:
                result.append("Seven")
            elif num == 8:
                result.append("Eight")
            elif num == 9:
                result.append("Nine")
        # If the number is not between 1 and 9, just add the number as a string to the output array
        else:
            result.append(str(num))

    # Return the sorted, reversed array
    return result
