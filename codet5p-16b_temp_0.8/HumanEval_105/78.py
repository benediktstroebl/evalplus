
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

    
    arr.sort(key=int)
    reverse_array = arr[::-1]
    return_array = []
    
    if arr:
        for i in range(len(reverse_array)):
            reverse_array[i] = str(reverse_array[i])
        
        for i in range(len(reverse_array)):
            if reverse_array[i].isdigit():
                if int(reverse_array[i]) == 1:
                    return_array.append("One")
                elif int(reverse_array[i]) == 2:
                    return_array.append("Two")
                elif int(reverse_array[i]) == 3:
                    return_array.append("Three")
                elif int(reverse_array[i]) == 4:
                    return_array.append("Four")
                elif int(reverse_array[i]) == 5:
                    return_array.append("Five")
                elif int(reverse_array[i]) == 6:
                    return_array.append("Six")
                elif int(reverse_array[
