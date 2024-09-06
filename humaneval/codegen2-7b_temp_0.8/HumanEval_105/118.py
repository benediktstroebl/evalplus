
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
    arr = sorted(arr)
    arr.reverse()
    
    if len(arr) == 0:
        return []
    
    if len(arr) == 1:
        return arr
    
    return [
        {
            "value": 1,
            "name": "One",
        },
        {
            "value": 2,
            "name": "Two",
        },
        {
            "value": 3,
            "name": "Three",
        },
        {
            "value": 4,
            "name": "Four",
        },
        {
            "value": 5,
            "name": "Five",
        },
        {
            "value": 6,
            "name": "Six",
        },
        {
            "value": 7,
            "name": "Seven",
        },
        {
            "value": 8,
            "name": "Eight",
        },
        {
            "value": 9,
            "name": "Nine",
        },
    ]

