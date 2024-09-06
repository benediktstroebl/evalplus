
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
    # Define a new variable that holds the value of the digit 
    # between 1 and 9 (inclusive) that you will search for in your array
    # for each iteration of your loop:
    dig = 1
    
    # Initialize an empty array that will hold the final names:
    names = []
    
    # Use a for loop to iterate through the provided array:
    for i in arr:
        # Inside your loop, write an if statement that checks to see if your digit is between 1 and 9 (inclusive) and is found in your array.
        # In this if statement, add the name of the digit to the final names array.
        if dig >= 1 and dig <= 9:
            # In your if statement, write a conditional expression that will check if the digit in your array is equal to the digit that you are searching for.
            # If it is, add the name of this digit to the names array.
            if i == dig:
                names.append("One")
            elif i == dig + 1:
                names.append("Two")
            elif i == dig + 2:
                names.append("Three")
            elif i == dig + 3:
                names.append("Four")
            elif i == dig + 4:
                names.append("Five")
            elif i == dig + 5:
                names.append("Six")
            elif i == dig + 6:
                names.append("Seven")
            elif i == dig + 7:
                names.append("Eight")
            elif i == dig + 8:
                names.append("Nine")
            # Else, continue looping.
            else:
                continue
        # Increment your digit by 1 each time your loop runs.
        dig += 1
    
    # Return the final names array:
    return names
    
