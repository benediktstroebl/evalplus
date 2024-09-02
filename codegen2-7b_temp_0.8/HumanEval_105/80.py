
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
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0]]
    
    new_arr = []
    for i in arr:
        new_arr.append(i)
    new_arr.sort()
    new_arr.reverse()
    
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    for i in new_arr:
        for name in names:
            if i == name:
                new_arr[new_arr.index(i)] = name
                break
    
    return new_
