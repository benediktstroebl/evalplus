
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
    digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    by_length_dict = dict(zip(range(10), digits[1:]))
    # using dict to map by_length_dict['1'] = 'One' and so on
    
    if len(arr) == 0:
        return []
    
    res = []
    sorted_arr = sorted(arr, key=lambda x: abs(x))
    reversed_arr = sorted_arr[::-1]
    
    for i in reversed_arr:
        if i < 0 or i > 9:
            res.append(digits[0])
        else:
            res.append(by_length_dict[i])
    return res

