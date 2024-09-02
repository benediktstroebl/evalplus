
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

    arr.sort()
    arr.reverse()
    arr = [str(i) for i in arr]
    
    return [i if int(i) < 10 else "Ten" if int(i) == 10 else "Eleven" if int(i) == 11 else "Twelve" if int(i) == 12 else "Thirteen" if int(i) == 13 else "Fourteen" if int(i) == 14 else "Fifteen" if int(i) == 15 else "Sixteen" if int(i) == 16 else "Seventeen" if int(i) == 17 else "Eighteen" if int(i) == 18 else "Nineteen" for i in arr]
