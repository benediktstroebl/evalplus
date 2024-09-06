
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
    new_arr = []

    for i in sorted(arr):
        if i in range(1, 10):
            new_arr.append(str(i))

    for i in range(len(new_arr) -1, -1, -1):
        new_arr[i] = str(new_arr[i])

    for i in range(len(new_arr) -1, -1, -1):
        if new_arr[i] == "1":
            new_arr[i] = "One"
        if new_arr[i] == "2":
            new_arr[i] = "Two"
        if new_arr[i] == "3":
            new_arr[i] = "Three"
        if new_arr[i] == "4":
            new_arr[i] = "Four"
        if new_arr[i] == "5":
            new_arr[i] = "Five"
        if new_arr[i] == "6":
            new_arr[i] = "Six"
        if new_arr[i] == "7":
            new_arr[i] = "Seven"
        if new_arr[i] == "8":
            new_arr[i] = "Eight"
        if new_arr[i] == "9":
            new_arr[i] = "Nine"

    return new_arr
