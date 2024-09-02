
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
    if arr == []:
        return []
    arr.sort()
    arr.reverse()
    new_arr = []
    for num in arr:
        if 1 <= num <= 9:
            new_arr.append("One")
        elif 10 <= num <= 19:
            new_arr.append("Two")
        elif 20 <= num <= 99:
            new_arr.append("Three")
        elif 100 <= num <= 999:
            new_arr.append("Four")
        elif 1000 <= num <= 9999:
            new_arr.append("Five")
        elif 10000 <= num <= 99999:
            new_arr.append("Six")
        elif 100000 <= num <= 999999:
            new_arr.append("Seven")
        elif 1000000 <= num <= 9999999:
            new_arr.append("Eight")
        elif 1000000000 <= num <= 99999999:
            new_arr.append("Nine")
        elif num == 0:
            new_arr.append("Zero")
        else:
            new_arr.append(str(num))
    return new_arr


