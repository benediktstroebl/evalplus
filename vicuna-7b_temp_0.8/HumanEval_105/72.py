
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
    # Get the array in a list of integers
    integers = list(arr)
    # Create a dictionary that maps the digits to the names
    digits_to_names = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}
    # Create a list of strings that will hold the sorted and reversed list of integers
    sorted_names = []
    # Sort the integers and get the list of sorted integers
    sorted_list = sorted(integers)
    # Reverse the sorted list
    reversed_list = [integers.index(i) for i in sorted_list]
    # Iterate through the sorted and reversed list
    for i in range(len(sorted_names)):
        # Get the first number of the pair
        first_number = sorted_list[reversed_list[i]]
        # Get the second number of the pair
        second_number = sorted_list[reversed_list[i+1]]
        # Get the name of the number
        name = digits_to_names[str(first_number)]
        # Add the name to the list
        sorted_names.append(name)
    return sorted_names
