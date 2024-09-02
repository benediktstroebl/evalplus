
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

    
    
    def check_number(x):
        for i in range(1, 10):
            if i == x:
                return "One"
            if i == 10:
                return "Ten"
            if i == 11:
                return "Eleven"
            if i == 12:
                return "Twelve"
            if i == 13:
                return "Thirteen"
            if i == 14:
                return "Fourteen"
            if i == 15:
                return "Fifteen"
            if i == 16:
                return "Sixteen"
            if i == 17:
                return "Seventeen"
            if i == 18:
                return "Eighteen"
            if i == 19:
                return "Nineteen"
        
        
    def sorting(arr):
        arr.sort()
        arr.reverse()
        return arr
    
    
    if len(arr) == 0:
        return arr
    
    sorted_arr = sorting(arr)
    
    new_arr = []
    for x in sorted_arr:
        if x
