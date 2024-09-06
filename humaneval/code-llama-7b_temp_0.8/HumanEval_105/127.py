
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

    arr_of_index = []

    for i in range(len(arr)):
        if arr[i] in range(1, 10):
            arr_of_index.append([arr[i], i])

    arr_of_index.sort()
    arr_of_index.reverse()

    arr_of_names = []

    for item in arr_of_index:
        arr_of_names.append(str(item[0]))

    return ["One" if str(arr_of_names[0]) == "1" else
            "Two" if str(arr_of_names[1]) == "2" else
            "Three" if str(arr_of_names[2]) == "3" else
            "Four" if str(arr_of_names[3]) == "4" else
            "Five" if str(arr_of_names[4]) == "5" else
            "Six" if str(arr_of_names[5]) == "6" else
            "Seven" if str(arr_of_names[6]) == "7" else
            "Eight" if str(arr_of_names[7]) == "8" else
            "Nine" if str(arr_of_names[8]) == "9" else str(arr_of_names[i]) for i in range(len(arr_of_names))]
