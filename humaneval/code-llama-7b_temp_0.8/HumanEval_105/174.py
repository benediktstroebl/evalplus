
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
    
    # initialize new array
    output = []
    
    # sort the array
    sorted_arr = sorted(arr)
    
    # iterate through sorted array
    for i in sorted_arr:
        # check if number is between 1 and 9
        if i <= 9 and i >= 1:
            # append number to new array in string form
            output.append(str(i))
        
        # check if number is 0, 10, or 11
        elif i == 10:
            # append number to new array
            output.append("One")
        elif i == 0:
            # append number to new array
            output.append("Zero")
        elif i == 11:
            # append number to new array
            output.append("Eleven")
    
    # reverse array
    output.reverse()
    
    # loop through array and replace numbers with names
    for i in range(0, len(output)):
        if output[i] == "1":
            output[i] = "One"
        elif output[i] == "2":
            output[i] = "Two"
        elif output[i] == "3":
            output[i] = "Three"
        elif output[i] == "4":
            output[i] = "Four"
        elif output[i] == "5":
            output[i] = "Five"
        elif output[i] == "6":
            output[i] = "Six"
        elif output[i] == "7":
            output[i] = "Seven"
        elif output[i] == "8":
            output[i] = "Eight"
        elif output[i] == "9":
            output[i] = "Nine"
    
    # return output array
    return output
