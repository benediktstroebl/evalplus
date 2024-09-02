
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
    
    arr = [str(num) for num in arr if num in range(1, 10)]
    arr.sort(reverse=True)
    arr = [str(num) for num in arr]
    for num in arr:
        if num == "1":
            arr[arr.index(num)] = "One"
        elif num == "2":
            arr[arr.index(num)] = "Two"
        elif num == "3":
            arr[arr.index(num)] = "Three"
        elif num == "4":
            arr[arr.index(num)] = "Four"
        elif num == "5":
            arr[arr.index(num)] = "Five"
        elif num == "6":
            arr[arr.index(num)] = "Six"
        elif num == "7":
            arr[arr.index(num)] = "Seven"
        elif num == "8":
            arr[arr.index(num)] = "Eight"
        elif num == "9":
            arr[arr.index(num)] = "Nine"
    return arr




