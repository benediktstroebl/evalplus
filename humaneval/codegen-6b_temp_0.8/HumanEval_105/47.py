
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
    output = []

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [str(arr[0])]
    elif len(arr) == 2 and arr[0] < 1 and arr[1] > 9:
        return ['One']
    elif len(arr) == 2 and arr[0] < 1 and arr[1] < 1:
        return ['One']
    elif len(arr) == 2 and arr[0] < 1 and arr[1] == 1:
        return ['One', 'One']
    elif len(arr) == 2 and arr[0] < 1 and arr[1] > 9:
        return ['One', 'One']
    elif len(arr) == 2 and arr[0] > 9 and arr[1] < 1:
        return ['One', 'One']
    elif len(arr) == 2 and arr[0] > 9 and arr[1] > 9:
        return ['One', 'One']

    for num in arr:
        if num == 0 or num > 9:
            return []

    for num in arr:

        if num == 1:
            output += ['One']
        elif num == 2:
            output += ['Two']
        elif num == 3:
            output += ['Three']
        elif num == 4:
            output += ['Four']
        elif num == 5:
            output += ['Five']
        elif num == 6:
            output += ['Six']
        elif num == 7:
            output += ['Seven']
        elif num == 8:
            output += ['Eight']
        elif num == 9:
            output += ['Nine']


    return output

