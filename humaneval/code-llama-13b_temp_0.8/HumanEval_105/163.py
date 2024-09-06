
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

    arr.sort()
    arr.reverse()
    arr_of_str = []
    for item in arr:
        if 1 <= item <= 9:
            arr_of_str.append(str(item))
        else:
            arr_of_str.append(str(arr.count(item)))
    
    for i, item in enumerate(arr_of_str):
        if item == '1':
            arr_of_str[i] = 'One'
        if item == '2':
            arr_of_str[i] = 'Two'
        if item == '3':
            arr_of_str[i] = 'Three'
        if item == '4':
            arr_of_str[i] = 'Four'
        if item == '5':
            arr_of_str[i] = 'Five'
        if item == '6':
            arr_of_str[i] = 'Six'
        if item == '7':
            arr_of_str[i] = 'Seven'
        if item == '8':
            arr_of_str[i] = 'Eight'
        if item == '9':
            arr_of_str[i] = 'Nine'
    
    return arr_of_str
    
