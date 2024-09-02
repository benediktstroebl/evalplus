
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
    # Prepare the dictionary for mapping integer to its name.
    digit_to_name_mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # Create a new list to store the result.
    result = []
    
    # Iterate the arr.
    for num in arr:
        
        # If the number is between 1 and 9, push the name of the number to the result list.
        # We only need to push the names that are not None.
        if 1 <= num <= 9 and num in digit_to_name_mapping:
            result.append(digit_to_name_mapping[num])
    
    # Reverse the list result.
    result = result[::-1]
    
    # Return the result.
    return result

