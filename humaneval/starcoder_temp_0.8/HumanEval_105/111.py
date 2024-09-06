
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
    result = []
    for i in arr:
        if 1<=i<=9:
            result.append(i)
    result.sort()
    result.reverse()
    for j in range(len(result)):
        if result[j] == 1:
            result[j] = 'One'
        elif result[j] == 2:
            result[j] = 'Two'
        elif result[j] == 3:
            result[j] = 'Three'
        elif result[j] == 4:
            result[j] = 'Four'
        elif result[j] == 5:
            result[j] = 'Five'
        elif result[j] == 6:
            result[j] = 'Six'
        elif result[j] == 7:
            result[j] = 'Seven'
        elif result[j] == 8:
            result[j] = 'Eight'
        elif result[j] == 9:
            result[j] = 'Nine'
    return result
