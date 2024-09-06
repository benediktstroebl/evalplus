
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
    for num in arr:
        if num >= 1 and num <= 9:
            result.append(num)
    result = sorted(result)
    result = result[::-1]
    print(result)
    for num in result:
        if num == 1:
            result[result.index(num)] = 'One'
        if num == 2:
            result[result.index(num)] = 'Two'
        if num == 3:
            result[result.index(num)] = 'Three'
        if num == 4:
            result[result.index(num)] = 'Four'
        if num == 5:
            result[result.index(num)] = 'Five'
        if num == 6:
            result[result.index(num)] = 'Six'
        if num == 7:
            result[result.index(num)] = 'Seven'
        if num == 8:
            result[result.index(num)] = 'Eight'
        if num == 9:
            result[result.index(num)] = 'Nine'
    return result

