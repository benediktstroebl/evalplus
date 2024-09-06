
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
    if not arr:
        return []
    max_len = max(len(x) for x in arr)
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    result = []
    i = j = 0
    while i < len(arr) - 1:
        if arr[i] >= 1 and arr[i] <= 9:
            result.append(str(arr[i]))
            i += 1
        elif arr[i] < 1 or arr[i] > 9:
            break
        elif (arr[i] - 1) % 10 != 0:
            break
        i += 1
    while j < len(arr):
        if arr[j] >= 1 and arr[j] <= 9:
            result.append(str(arr[j]))
            j += 1
        elif arr[j] < 1 or arr[j] > 9:
            break
        else:
            result.append(names[i // 10])
            j += 1
    return result

arr = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr))
