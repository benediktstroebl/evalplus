
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
    
    def names(num):
        if num == 0:
            return ""
        else:
            return f"{num % 10}".replace("0", "One").replace("1", "Two").replace("2", "Three").replace("3", "Four").replace("4", "Five").replace("5", "Six").replace("6", "Seven").replace("7", "Eight").replace("8", "Nine").replace("9", "Ten")
    
    return sorted(arr, key=len, reverse=True) + [names(num) for num in arr if len(str(num)) > 1
