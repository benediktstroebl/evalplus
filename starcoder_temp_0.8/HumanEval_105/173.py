
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
    
    # This is the edge case, and will return an empty list
    if len(arr) == 0:
        return arr
    
    # First, we will do an inplace sort, so that all the values between 1 and 9 are at the front
    # and the values outside of that range are at the back.
    arr.sort()
    
    # Now, we will iterate through the list, and if we find a value that is in the range of 1 and 9,
    # we will replace the value with the correct string value.  We will convert it to a string using str(),
    # so that we can use it as a key to a dictionary.
    
    for i in range(len(arr)):
        if (arr[i] >= 1 and arr[i] <= 9):
            arr[i] = str(word_for_num[arr[i]])
            
    # Lastly, we will do an inplace reverse, so that the values inside the range of 1 and 9 are back at the front.
    arr.reverse()
    
    return arr
