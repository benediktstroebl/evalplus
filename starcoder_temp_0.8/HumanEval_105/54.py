
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
    # remove any weird numbers in the array
    arr = [x for x in arr if x >= 1 and x <= 9]

    # sort the numbers between 1 and 9 in the array
    arr.sort()

    # reverse the sorted array
    arr.reverse()

    # change each number to its corresponding name
    # from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    arr = [str(x) for x in arr]

    # append the name in front of the number
    # (e.g. change "1" to "One")
    for i in range(len(arr)):
        if arr[i].isdigit():
            arr[i] = "One" if int(arr[i]) == 1 else "Two" \
                if int(arr[i]) == 2 else "Three" if int(arr[i]) == 3 \
                else "Four" if int(arr[i]) == 4 else "Five" if int(arr[i]) == 5 \
                else "Six" if int(arr[i]) == 6 else "Seven" if int(arr[i]) == 7 \
                else "Eight" if int(arr[i]) == 8 else "Nine"

    return arr
