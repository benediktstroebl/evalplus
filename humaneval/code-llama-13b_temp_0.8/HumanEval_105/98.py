
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
    # print(arr)
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return ['One' if arr[0] == 1 else 'Two' if arr[0] == 2 else 'Three' if arr[0] == 3 else 'Four' if arr[0] == 4 else 'Five' if arr[0] == 5 else 'Six' if arr[0] == 6 else 'Seven' if arr[0] == 7 else 'Eight' if arr[0] == 8 else 'Nine']
    
    res = []
    for e in sorted(arr, reverse=True):
        if e in [1,2,3,4,5,6,7,8,9]:
            res.append('One' if e == 1 else 'Two' if e == 2 else 'Three' if e == 3 else 'Four' if e == 4 else 'Five' if e == 5 else 'Six' if e == 6 else 'Seven' if e == 7 else 'Eight' if e == 8 else 'Nine')
    return res
