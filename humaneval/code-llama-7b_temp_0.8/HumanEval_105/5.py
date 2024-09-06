
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
    ###########################
    # 1) Reverse the given array
    ###########################
    result_arr = arr[::-1]

    ###########################
    # 2) Create an array that has name for each digit
    #    If the digit is not from 1 to 9, return the digit as a string
    #    For example: 0 --> 'Zero', 1 --> 'One', 2 --> 'Two' ...
    ###########################
    name_arr = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    
    ###########################
    # 3) Go over the result arr and replace each digit with name
    #    If the digit is from 1 to 9, replace it with its name
    #    If the digit is not from 1 to 9, return the digit as a string
    ###########################
    result = []
    for digit in result_arr:
        if digit >= 1 and digit <= 9:
            result.append(name_arr[digit])
        else:
            result.append(str(digit))
    
    return result
