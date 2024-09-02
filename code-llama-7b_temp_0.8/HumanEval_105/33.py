
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
    # sort and reverse the array
    arr.sort()
    arr.reverse()
    # string to array 
    arr_str = list(map(str,arr))
    # remove non digit elements
    arr_str = list(filter(lambda x: x in '123456789', arr_str))
    # convert digit to name
    digits_name = {}
    digits_name["1"] = "One"
    digits_name["2"] = "Two"
    digits_name["3"] = "Three"
    digits_name["4"] = "Four"
    digits_name["5"] = "Five"
    digits_name["6"] = "Six"
    digits_name["7"] = "Seven"
    digits_name["8"] = "Eight"
    digits_name["9"] = "Nine"
    arr_str_name = [digits_name[item] for item in arr_str]
    return arr_str_name
    















