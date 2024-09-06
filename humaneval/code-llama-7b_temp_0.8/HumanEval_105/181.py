
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
    # create a list to store the results 
    output = []
    
    # check if arr is empty
    if arr == []:
        return []
    
    # sort the array 
    arr.sort()
    
    # reverse the sorted arr
    arr.reverse()
    
    # loop through the arr
    for number in arr:
        
        # check if the number is between 1 and 9 inclusive
        if (number <= 9) and (number >= 1):
            
            # check if the number is 1
            if number == 1:
                
                # append the corresponding string to the output
                output.append("One")
                
            # check if the number is 2
            if number == 2:
                
                # append the corresponding string to the output
                output.append("Two")
                
            # check if the number is 3
            if number == 3:
                
                # append the corresponding string to the output
                output.append("Three")
                
            # check if the number is 4
            if number == 4:
                
                # append the corresponding string to the output
                output.append("Four")
                
            # check if the number is 5
            if number == 5:
                
                # append the corresponding string to the output
                output.append("Five")
                
            # check if the number is 6
            if number == 6:
                
                # append the corresponding string to the output
                output.append("Six")
                
            # check if the number is 7
            if number == 7:
                
                # append the corresponding string to the output
                output.append("Seven")
                
            # check if the number is 8
            if number == 8:
                
                # append the corresponding string to the output
                output.append("Eight")
                
            # check if the number is 9
            if number == 9:
                
                # append the corresponding string to the output
                output.append("Nine")
        
        # check if the number is not between 1 and 9 inclusive
        else:
            
            # append the
