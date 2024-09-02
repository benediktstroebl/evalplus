
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

    # Create a list of the possible numbers 
    # and their names as strings
    num_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Get the list of numbers from 1-9
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Convert the numbers to strings
    string_numbers = [str(n) for n in numbers]

    # Filter out the numbers that are not 1-9
    # i.e. 0, 10
    filtered_arr = [el for el in arr if el in numbers]

    # Sort the list
    sorted_list = sorted(filtered_arr, reverse=True)

    # Use the dictionary and the list to convert the numbers
    # to their corresponding name
    # Return the resulting array
    return [num_names[int(n)] for n in sorted_list]
