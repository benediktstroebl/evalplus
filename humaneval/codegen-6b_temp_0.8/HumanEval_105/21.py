
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
    # set up the counter and result
    res = []
    counter = 0

    # loop through the array, checking for each integer
    for num in arr:
        # check if the integer is 1-9
        if 1 <= num <= 9:
            # add the name to the result array
            res.append(str(num))
            # increment the counter
            counter += 1
    
    # reverse the array
    res = res[::-1]
    
    # for each integer, convert it to the correct name and add it to the result
    for i in range(counter):
        res[i] = int_to_name(res[i])

    return res

