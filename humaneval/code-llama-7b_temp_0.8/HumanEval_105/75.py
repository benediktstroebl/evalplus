
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
    # TODO: Write your solution here
    # print(arr)
    if len(arr) == 0:
        return []
    for i in range(len(arr)):
        if arr[i] < 1 or arr[i] > 9:
            arr.pop(i)
    
    arr.sort()
    # print(arr)
    arr.reverse()
    # print(arr)
    str_arr = []
    for i in range(len(arr)):
        if arr[i] == 1:
            str_arr.append("One")
        if arr[i] == 2:
            str_arr.append("Two")
        if arr[i] == 3:
            str_arr.append("Three")
        if arr[i] == 4:
            str_arr.append("Four")
        if arr[i] == 5:
            str_arr.append("Five")
        if arr[i] == 6:
            str_arr.append("Six")
        if arr[i] == 7:
            str_arr.append("Seven")
        if arr[i] == 8:
            str_arr.append("Eight")
        if arr[i] == 9:
            str_arr.append("Nine")
    return str_arr

