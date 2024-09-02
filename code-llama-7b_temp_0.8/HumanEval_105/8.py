
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
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    # valid only for 1-9 numbers
    # 1000 is a valid number and it's less than 10000
    # also for 11, 111, 1111
    arr = [int(x) for x in str(sum(arr)) if x in "123456789"]
    arr.sort()
    arr.reverse()
    # join with strings and make a dictionary
    # the reverse is to do a simple loop instead of using a dictionary
    # with this way the elements can be accessed with the key name
    arr = {i: x for i, x in enumerate(arr, 1)}
    names = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    arr = [names[str(arr[x])] for x in arr]
    return arr

