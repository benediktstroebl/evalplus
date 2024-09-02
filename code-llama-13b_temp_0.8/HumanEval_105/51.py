
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
    return [
        name 
        for number in arr
        for name in [
            'One' if number == 1 else
            'Two' if number == 2 else
            'Three' if number == 3 else
            'Four' if number == 4 else
            'Five' if number == 5 else
            'Six' if number == 6 else
            'Seven' if number == 7 else
            'Eight' if number == 8 else
            'Nine' if number == 9 else ''
        ]
        if name != ''
    ][::-1] if arr else []

