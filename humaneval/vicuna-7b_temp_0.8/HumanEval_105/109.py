
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
    
    n = len(arr)
    if n == 1:
        return [arr[0]]

    if n > 0:
        i = 0
        while i < n / 2:
            if arr[i] >= 1 and arr[i] <= 9:
                j = i + 1
                while j < n and arr[j] >= 1 and arr[j] <= 9:
                    j += 1
                if j > i:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                else:
                    break
        n -= 1

    return list(map(lambda x: word_to_number[x], reversed(arr)))