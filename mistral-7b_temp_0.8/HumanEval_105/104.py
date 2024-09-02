
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
    # Pseudocode:
    # 1) make an array to return and a list to add numbers to
    # 2) loop through array
    #   2a) if number is less than 10 and greater than 0 add to list
    # 3) reverse list
    # 4) convert list to strings
    # 5) add numbers to return array
    # 6) return array
    #
    # Code:
    arr = []
    list_num = []
    for num in arr:
        if num < 10 and num > 0:
            list_num.append(num)
    list_num.reverse()
    for num in list_num:
        if num == 1:
            arr.append("One")
        elif num == 2:
            arr.append("Two")
        elif num == 3:
            arr.append("Three")
        elif num == 4:
            arr.append("Four")
        elif num == 5:
            arr.append("Five")
        elif num == 6:
            arr
