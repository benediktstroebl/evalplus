
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
    if not arr:
        return []
    
    numbers = {}
    for num in range(1, 10):
        numbers[num] = str(num)
    
    numbers[10] = 'Ten'
    numbers[11] = 'Eleven'
    numbers[12] = 'Twelve'
    numbers[13] = 'Thirteen'
    numbers[14] = 'Fourteen'
    numbers[15] = 'Fifteen'
    numbers[16] = 'Sixteen'
    numbers[17] = 'Seventeen'
    numbers[18] = 'Eighteen'
    numbers[19] = 'Nineteen'
    
    numbers[20] = 'Twenty'
    numbers[30] = 'Thirty'
    numbers[40] = 'Forty'
    numbers[50] = 'Fifty'
    numbers[60] = 'Sixty'
    numbers[70] = 'Seventy'
    numbers[80] = 'Eighty'
    numbers[90] = 'Ninety'
    
    numbers[100] = 'One Hundred'
    numbers[200] = 'Two Hundred'
    numbers[300] = 'Three Hundred'
    numbers[400] = 'Four Hundred'
    numbers[500] = 'Five Hundred'
    numbers[600] = 'Six Hundred'
    numbers[700] = 'Seven Hundred'
    numbers[800] = 'Eight Hundred'
    numbers[900] = 'Nine Hundred'
    
    sorted_arr = sorted(arr)
    reverse_arr = sorted_arr[::-1]
    return [numbers[num] for num in reverse_arr]

    
