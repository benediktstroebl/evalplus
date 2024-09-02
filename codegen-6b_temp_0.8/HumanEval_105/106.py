
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
    arr.sort()
    arr.reverse()
    converted_numbers = []
    for i in arr:
        if i >= 1 and i <= 9:
            converted_numbers.append(i)
        else:
            pass
    final_number_string = []
    for i in converted_numbers:
        if i == 1:
            final_number_string.append("One")
        elif i == 2:
            final_number_string.append("Two")
        elif i == 3:
            final_number_string.append("Three")
        elif i == 4:
            final_number_string.append("Four")
        elif i == 5:
            final_number_string.append("Five")
        elif i == 6:
            final_number_string.append("Six")
        elif i == 7:
            final_number_string.append("Seven")
        elif i == 8:
            final_number_string.append("Eight")
        elif i == 9:
            final_number_string.append("Nine")
    return final_number_string
