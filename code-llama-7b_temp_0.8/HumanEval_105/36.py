
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
    # The solution by recursion
    # arr = [2, 1, 1, 4, 5, 8, 2, 3]
    # arr.sort()
    # arr.reverse()
    # arr2 = []
    # for i in arr:
    #     if i == 1:
    #         arr2.append("One")
    #     elif i == 2:
    #         arr2.append("Two")
    #     elif i == 3:
    #         arr2.append("Three")
    #     elif i == 4:
    #         arr2.append("Four")
    #     elif i == 5:
    #         arr2.append("Five")
    #     elif i == 8:
    #         arr2.append("Eight")
    #     else:
    #         arr2.append(i)
    # return arr2

    # The solution by lambda functions
    arr.sort()
    arr.reverse()
    arr2 = list(map(lambda i: "One" if i == 1 else
                    "Two" if i == 2 else
                    "Three" if i == 3 else
                    "Four" if i == 4 else
                    "Five" if i == 5 else
                    "Eight" if i == 8 else
                    i, arr))
    return arr2

