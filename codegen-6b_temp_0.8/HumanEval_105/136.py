
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
    if not arr:
        return []
    
    # sort the array, return the array reversed
    arr.sort(reverse=True)
    return_arr = []

    for num in arr:
        if num > 0 and num <= 9:
            # by index to replace
            digit_index = num - 1
            return_arr.append(string_from_number_dict[digit_index])
        
        elif num == 0:
            # ignore 0
            pass
        
        elif num <= 0 and num >= -9:
            # reverse the array, then by index to replace
            arr_reverse = arr
            arr_reverse.reverse()
            num_reverse = num
            digit_index = arr_reverse.index(num_reverse)
            return_arr.append(string_from_number_dict[digit_index])
    
    return return_arr


assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
assert by_length([]) == []
assert by_length([-1, 1, 55]) == ['One']
assert by_length([-2, 2, 3]) == ['Two']
assert by_length([0, -1, 55]) == ['One', 'One']
assert by_length([1, 1, 1, 1]) == ['One', 'One', 'One', 'One']
assert by_length([2, 2, 2, 2]) == ['Two', 'Two', 'Two', 'Two']
assert by_length([10, 11, 12]) == ['One', 'One', 'Two']
assert by_length([-1, 1, 15]) == ['One', 'One', 'Three']
assert by_length([10, 11, 50]) == ['Two', 'Two']
assert by_length([10, 50, 11]) == ['Two', 'One']
