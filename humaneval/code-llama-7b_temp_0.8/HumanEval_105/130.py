
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
    # Sort array
    # Lengths of each number
    # Zip together
    # Reverse
    # Convert

    # Check for edge cases
    if not arr or max(arr) > 9 or min(arr) < 1:
        return []

    # Sort
    # Get number lengths
    length_dict = {
        len(str(num)) : num
        for num in arr
        if (num >= 1 and num <= 9)
    }

    # Sort
    sorted_lengths = sorted(length_dict.keys(), reverse = True)
    numbers = [length_dict[length] for length in sorted_lengths]

    # Reverse
    numbers.reverse()

    # Convert to names
    names = [
        "One" if num == 1 else "Two" if num == 2 else "Three" if num == 3 else 
        "Four" if num == 4 else "Five" if num == 5 else "Six" if num == 6 else 
        "Seven" if num == 7 else "Eight" if num == 8 else "Nine"
        for num in numbers
    ]

    return names

