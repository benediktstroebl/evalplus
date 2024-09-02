
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
    sorted_arr = []
    for i in range(len(arr)):
        if arr[i] >= 1 and arr[i] <= 9:
            sorted_arr.append(arr[i])
    sorted_arr.sort()
    sorted_arr.reverse()
    name_arr = []
    for j in range(len(sorted_arr)):
        if sorted_arr[j] == 1:
            name_arr.append("One")
        elif sorted_arr[j] == 2:
            name_arr.append("Two")
        elif sorted_arr[j] == 3:
            name_arr.append("Three")
        elif sorted_arr[j] == 4:
            name_arr.append("Four")
        elif sorted_arr[j] == 5:
            name_arr.append("Five")
        elif sorted_arr[j] == 6:
            name_arr.append("Six")
        elif sorted_arr[j] == 7:
           
