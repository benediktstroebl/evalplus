
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
    
    for number in arr:
        if 1 <= number <= 9:
            result.append(str(number))
    
    result.sort(reverse = True)
    result = result[::-1]
    
    replace_numbers = []
    
    for number in result:
        if number == '1':
            replace_numbers.append('One')
        elif number == '2':
            replace_numbers.append('Two')
        elif number == '3':
            replace_numbers.append('Three')
        elif number == '4':
            replace_numbers.append('Four')
        elif number == '5':
            replace_numbers.append('Five')
        elif number == '6':
            replace_numbers.append('Six')
        elif number == '7':
            replace_numbers.append('Seven')
        elif number == '8':
            replace_numbers.append('Eight')
        elif number == '9':
            replace_numbers.append('Nine')
    
