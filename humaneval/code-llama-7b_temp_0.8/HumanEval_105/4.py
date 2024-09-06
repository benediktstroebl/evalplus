
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
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def reverse(start, end):
        while start < end:
            swap(start, end)
            start += 1
            end -= 1

    result = []
    i = 0
    while i < len(arr):
        if arr[i] > 0 and arr[i] < 10:
            result.append(arr[i])
        else:
            arr.pop(i)
        i += 1
    
    length = len(result)
    if length == 0:
        return []

    for i in range(length):
        if result[i] == 1:
            result[i] = "One"
        elif result[i] == 2:
            result[i] = "Two"
        elif result[i] == 3:
            result[i] = "Three"
        elif result[i] == 4:
            result[i] = "Four"
        elif result[i] == 5:
            result[i] = "Five"
        elif result[i] == 6:
            result[i] = "Six"
        elif result[i] == 7:
            result[i] = "Seven"
        elif result[i] == 8:
            result[i] = "Eight"
        elif result[i] == 9:
            result[i] = "Nine"

    reverse(0, length - 1)
    return result

