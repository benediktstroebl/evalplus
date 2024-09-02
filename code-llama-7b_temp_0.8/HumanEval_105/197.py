
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
    def str_map(num):
        if num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        elif num == 9:
            return "Nine"
        else:
            return num

    if arr == []:
        return []

    arr = sorted(arr, reverse=True)
    #print(arr)
    arr = list(map(str_map, arr))
    return arr
