
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
    # Edge case
    if len(arr) == 0:
        return []
    
    # Store the values we're interested in
    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    # Convert array to numbers and remove elements outside of 1 - 9
    arr_num = []
    for num in arr:
        if num in number_dict:
            arr_num.append(num)
    
    # Sort the elements that are in the correct range
    arr_num.sort()
    arr_num.reverse()
    
    # Return the numbers as a word
    result = []
    for num in arr_num:
        word = "one" if num == 1 else "two" if num == 2 else "three" if num == 3 else "four" if num == 4 else "five" if num == 5 else "six" if num == 6 else "seven" if num == 7 else "eight" if num == 8 else "nine"
        result.append(word)
    
    return result

