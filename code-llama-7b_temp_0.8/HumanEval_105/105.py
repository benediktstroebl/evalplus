
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
    # My initial solution
    # if len(arr) == 0:
    #   return []
    
    # # Sort the array
    # sorted_arr = sorted(arr)
    
    # # Reverse the array
    # reverse_arr = sorted_arr[::-1]
    
    # # Convert the digits to names
    # new_arr = []
    # for i in range(len(reverse_arr)):
    #     if reverse_arr[i] == 1:
    #         new_arr.append("One")
    #     if reverse_arr[i] == 2:
    #         new_arr.append("Two")
    #     if reverse_arr[i] == 3:
    #         new_arr.append("Three")
    #     if reverse_arr[i] == 4:
    #         new_arr.append("Four")
    #     if reverse_arr[i] == 5:
    #         new_arr.append("Five")
    #     if reverse_arr[i] == 6:
    #         new_arr.append("Six")
    #     if reverse_arr[i] == 7:
    #         new_arr.append("Seven")
    #     if reverse_arr[i] == 8:
    #         new_arr.append("Eight")
    #     if reverse_arr[i] == 9:
    #         new_arr.append("Nine")
    
    # return new_arr

    # Yongjun's solution
    if len(arr) == 0:
        return []

    arr = sorted(arr)
    arr.reverse()
    result = []
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] < 10:
            result.append(str(arr[i]) + " -> " + "One" if arr[i] == 1 else "Two" if arr[i] == 2 else "Three" if arr[i] == 3 else "Four" if arr[i] == 4 else "Five" if arr[i] ==
