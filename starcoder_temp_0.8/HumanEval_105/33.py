
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
    # implement this function
    # Your code here
    tempArr = []
    resultArr = []
    for x in arr:
        if (1 <= x <= 9):
            tempArr.append(x)
    tempArr.sort(reverse=True)
    for y in tempArr:
        if (y == 1):
            resultArr.append("One")
        elif (y == 2):
            resultArr.append("Two")
        elif (y == 3):
            resultArr.append("Three")
        elif (y == 4):
            resultArr.append("Four")
        elif (y == 5):
            resultArr.append("Five")
        elif (y == 6):
            resultArr.append("Six")
        elif (y == 7):
            resultArr.append("Seven")
        elif (y == 8):
            resultArr.append("Eight")
        elif (y == 9):
            resultArr.append("Nine")
    return resultArr

