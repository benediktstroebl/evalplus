
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
    
    if arr == []:
        return []
    elif arr.count(9) > 1 or arr.count(8) > 1 or arr.count(7) > 1 or arr.count(6) > 1 or arr.count(5) > 1 or arr.count(4) > 1 or arr.count(3) > 1 or arr.count(2) > 1 or arr.count(1) > 1:
        return ['One']
    
    elif arr.count(9) == 1 and arr.count(8) == 1 and arr.count(7) == 1 and arr.count(6) == 1 and arr.count(5) == 1 and arr.count(4) == 1 and arr.count(3) == 1 and arr.count(2) == 1 and arr.count(1) == 1:
        arr.sort()
        arr.reverse()
        answer = []
        for i in range(0, len(arr)):
            if arr[i] == 9:
                answer.append('Nine
