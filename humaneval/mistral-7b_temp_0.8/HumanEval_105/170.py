
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
    
    arr = arr.copy()
    one = ["Zero"]
    two = ["One", "Two"]
    three = ["One", "Two", "Three"]
    four = ["One", "Two", "Three", "Four"]
    five = ["One", "Two", "Three", "Four", "Five"]
    six = ["One", "Two", "Three", "Four", "Five", "Six"]
    seven = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
    eight = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
    nine = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    for x in arr:
        if x > 9 or x < 0:
            x = str(x)
            one.append(x)
        elif x in range(1,10):
            if x ==
