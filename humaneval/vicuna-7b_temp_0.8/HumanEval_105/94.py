
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
    n = len(arr)
    if n == 0:
        return []
    arr1 = []
    for i in range(n):
        arr1.append(arr[i])
        if i != n-1 and arr[i] != arr[i+1]:
            arr1.append(" ")
    result = []
    for i in arr1:
        if i == " " or i == "One" or i == "Two" or i == "Three" or i == "Four" or i == "Five" or i == "Six" or i == "Seven" or i == "Eight" or i == "Nine":
            result.append(i)
        else:
            result.append(to_name(i))
    return result