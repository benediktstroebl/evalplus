
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
    # Initialize the new array to return
    newArr = []
    # Loop through the array
    for num in arr:
        # If num is between 1 and 9
        if num >= 1 and num <= 9:
            # Get the position of the number in the array
            pos = num-1
            # Convert the position to a string
            string_num = str(pos)
            # If the number is between 1 and 3
            if num <= 3:
                # Append the name to the new array
                newArr.append(str(string_num) + "Three")
            # If the number is between 4 and 6
            elif num <= 6:
                # Append the name to the new array
                newArr.append(str(string_num) + "Six")
            # If the number is between 7 and 9
            elif num <= 9:
                # Append the name to the new array
                newArr.append(str(string_num) + "Nine")
    # Reverse the new array
    newArr.reverse()
    # Return the new array
    return newArr

