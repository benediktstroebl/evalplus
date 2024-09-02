
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
    
    # your code goes here
    
    # check if there is a digit between 1 and 9
    if (arr == []):
        return []

    # check if the length of the array is between 1 and 9
    if (len(arr) <= 0 or len(arr) > 9):
        return []

    # sort the array
    arr = sorted(arr)
    # reverse the array
    arr = arr[::-1]

    # initialize an empty list
    output = []

    # loop through the array and replace each digit with its corresponding name
    for i in range(len(arr)):
        if (arr[i] >= 1 and arr[i] <= 9):
            if (arr[i] == 1):
                output.append("One")
            elif (arr[i] == 2):
                output.append("Two")
            elif (arr[i] == 3):
                output.append("Three")
            elif (arr[i] == 4):
                output.append("Four")
