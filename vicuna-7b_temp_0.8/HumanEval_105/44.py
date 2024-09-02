
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
    # return []
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr[0]]
    else:
        digits = []
        reversed_arr = sorted(list(reversed(arr)))
        for i in range(len(reversed_arr)):
            digits.append(str(reversed_arr[i]))
        for i in range(len(digits)):
            if digits[i] == '1':
                digits[i] = 'One'
            elif digits[i] == '2':
                digits[i] = 'Two'
            elif digits[i] == '3':
                digits[i] = 'Three'
            elif digits[i] == '4':
                digits[i] = 'Four'
            elif digits[i] == '5':
                digits[i] = 'Five'
            elif digits[i] == '6':
                digits[i] = 'Six'
            elif digits[i] == '7':
                digits[i] = 'Seven'
            elif digits[i] == '8':
                digits[i] = 'Eight'
            elif digits[i] == '9':
                digits[i] = 'Nine'
        return digits
