
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
    
    def between_1_and_9(integer):
        if 1 <= integer <= 9:
            return True
        else:
            return False

    def reverse(arr):
        result = []
        for i in range(len(arr) - 1, -1, -1):
            result.append(arr[i])
        return result

    result = []
    for integer in arr:
        if between_1_and_9(integer):
            result.append(integer)
    
    result = sorted(result)
    result = reverse(result)

    result_name = []
    for i in result:
        if i == 1:
            result_name.append("One")
        elif i == 2:
            result_name.append("Two")
        elif i == 3:
            result_name.append("Three")
        elif i == 4:
            result_name.append("Four")
        elif i == 5:
            result_name.append("Five")
        elif i == 6:
            result_name.append("Six")
        elif i == 7:
            result_name.append("Seven")
        elif i == 8:
            result_name.append("Eight")
        elif i == 9:
            result_name.append("Nine")
        else:
            return []

    return result_name

