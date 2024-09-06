
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
    if len(arr) != 0:
        for number in arr:
            if number < 10 and number > 0 and number <= 9:
                result.append(number)

        result.sort(reverse = True)
        result.reverse()

        for digit in result:
            if digit == 1:
                result[result.index(digit)] = "One"
            elif digit == 2:
                result[result.index(digit)] = "Two"
            elif digit == 3:
                result[result.index(digit)] = "Three"
            elif digit == 4:
                result[result.index(digit)] = "Four"
            elif digit == 5:
                result[result.index(digit)] = "Five"
            elif digit == 6:
                result[result.index(digit)] = "Six"
            elif digit == 7:
                result[result.index(digit)] = "Seven"
            elif digit == 8:
                result[result.index(digit)] = "Eight"
            elif digit == 9:
                result[result.index(digit)] = "Nine"
    
    return result

