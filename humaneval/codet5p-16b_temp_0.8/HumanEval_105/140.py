
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

    
    def find_value(n):
        try:
            return int(n)
        except ValueError:
            if n == "One":
                return 1
            elif n == "Two":
                return 2
            elif n == "Three":
                return 3
            elif n == "Four":
                return 4
            elif n == "Five":
                return 5
            elif n == "Six":
                return 6
            elif n == "Seven":
                return 7
            elif n == "Eight":
                return 8
            elif n == "Nine":
                return 9
            else:
                return None

    return [find_value(n) for n in sorted(arr, reverse=True)]

