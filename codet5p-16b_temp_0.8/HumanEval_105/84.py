
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

    for i, x in enumerate(arr):
        if x > 9 or x < 0:
            del arr[i]
    
    arr = sorted(arr)
    arr = arr[::-1]
    arr = [str(x) for x in arr]

    return [chr(x) for x in range(65, 91)] if arr == ["0"] else ["Zero"] + ["One"]*8 + ["Two"]*7 + ["Three"]*6 + ["Four"]*5 + ["Five"]*4 + ["Six"]*3 + ["Seven"]*2 + ["Eight"]*1 + ["Nine"]*8
