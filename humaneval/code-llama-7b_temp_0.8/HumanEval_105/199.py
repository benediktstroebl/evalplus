
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
    # Edge cases
    if not isinstance(arr, list):
        return []
    if not arr:
        return []
    # Get all numbers between 1 and 9, and append them to a list
    digits = list(range(1, 10))
    # Sort the list
    arr.sort()
    # Initialize a new array
    new_arr = []
    # Iterate through the original array
    for i in arr:
        # If the number is between 1 and 9 append the name to the new array
        if i in digits:
            new_arr.append(str(i))
    # Iterate through the new array
    for j in range(len(new_arr)):
        # Replace the number with its corresponding name
        if new_arr[j] == "1":
            new_arr[j] = "One"
        elif new_arr[j] == "2":
            new_arr[j] = "Two"
        elif new_arr[j] == "3":
            new_arr[j] = "Three"
        elif new_arr[j] == "4":
            new_arr[j] = "Four"
        elif new_arr[j] == "5":
            new_arr[j] = "Five"
        elif new_arr[j] == "6":
            new_arr[j] = "Six"
        elif new_arr[j] == "7":
            new_arr[j] = "Seven"
        elif new_arr[j] == "8":
            new_arr[j] = "Eight"
        elif new_arr[j] == "9":
            new_arr[j] = "Nine"
    # Reverse the new array
    new_arr.reverse()
    # Iterate through the new array
    for k in range(len(new_arr)):
        # Replace the numbers with their names
        if new_arr[k] == "1":
            new_arr[k] = "One"
        elif new_arr[k] == "2":
            new_arr[k] = "Two"
        elif new_arr[k]
