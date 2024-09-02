
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
    # create an empty list
    result = []
    # if array is empty, return an empty array
    if not arr:
        return result
    # use the filter function to filter out any value not between 1 and 9
    filtered_arr = list(filter(lambda x: x >= 1 and x <= 9, arr))
    # use the sorted function to sort the filtered array
    sorted_arr = sorted(filtered_arr)
    # use the reverse function to reverse the sorted array
    reversed_arr = reversed(sorted_arr)
    # use the map function to map the reversed array
    digit_names = map(lambda x: str(x), reversed_arr)
    # use the join function to join the digit names into a list
    result = list(map(lambda x: name_of_digit(x), digit_names))
    # return the result list
    return result
