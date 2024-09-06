
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
    # if the array has any strange number ignore it
    if not arr:
        return []
    
    # sort the array
    arr.sort()
    
    # reverse the array
    arr.reverse()
    
    # get the index of each number
    for i, num in enumerate(arr):
        if num == 0:
            num = "Zero"
        elif num == 1:
            num = "One"
        elif num == 2:
            num = "Two"
        elif num == 3:
            num = "Three"
        elif num == 4:
            num = "Four"
        elif num == 5:
            num = "Five"
        elif num == 6:
            num = "Six"
        elif num == 7:
            num = "Seven"
        elif num == 8:
            num = "Eight"
        elif num == 9:
            num = "Nine"
        
        # replace each number by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
        arr[i] = num
    
    # return the new array
    return arr
