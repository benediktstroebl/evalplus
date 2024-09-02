
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
    
    # Function that checks if a number is between 1 and 9
    def check_num(number):
        if number >= 1 and number <= 9:
            return True
        else:
            return False

    # Create a new empty list
    sorted_array = []

    # If the array is empty, return the empty array
    if len(arr) == 0:
        return []
    
    # Iterate through the array and add each number to the sorted_array if it is between 1 and 9
    for num in arr:
        if check_num(num):
            sorted_array.append(num)

    # Sort the array
    sorted_array.sort()

    # Iterate through the array in reverse order and append the corresponding number to the final array
    # if the number is between 1 and 9
    reversed_array = []
    for num in sorted_array[::-1]:
        if num == 1:
            reversed_array.append("One")
        elif num == 2:
            reversed_array.append("Two")
        elif num == 3:
            reversed_array.append("Three")
        elif num == 4:
            reversed_array.append("Four")
        elif num == 5:
            reversed_array.append("Five")
        elif num == 6:
            reversed_array.append("Six")
        elif num == 7:
            reversed_array.append("Seven")
        elif num == 8:
            reversed_array.append("Eight")
        elif num == 9:
            reversed_array.append("Nine")

    return reversed_array
