
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

    
    
    def stringify(num):
        num = str(num)
        name = "Zero"
        if num == "1": name = "One"
        elif num == "2": name = "Two"
        elif num == "3": name = "Three"
        elif num == "4": name = "Four"
        elif num == "5": name = "Five"
        elif num == "6": name = "Six"
        elif num == "7": name = "Seven"
        elif num == "8": name = "Eight"
        elif num == "9": name = "Nine"
        return name
        
    
    if not arr:
        return []
    
    arr.sort()
    
    res = []
    
    for i in range(0, len(arr)):
        if arr[i] >= 1 and arr[i] <= 9:
            res.append(stringify(arr[i]))
        
    return res[::-1]
    
