
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
    if len(arr) == 0:
        return []
    
    short_digits = {}
    
    for n in range(1, 10):
        short_digits[n] = str(n)
    
    short_digits[10] = 'Ten'
    short_digits[11] = 'Eleven'
    short_digits[12] = 'Twelve'
    short_digits[13] = 'Thirteen'
    short_digits[14] = 'Fourteen'
    short_digits[15] = 'Fifteen'
    short_digits[16] = 'Sixteen'
    short_digits[17] = 'Seventeen'
    short_digits[18] = 'Eighteen'
    short_digits[19] = 'Nineteen'
    
    short_digits[20] = 'Twenty'
    short_digits[30] = 'Thirty'
    short_digits[40] = 'Forty'
    short_digits[50] = 'Fifty'
    short_digits[60] = 'Sixty'
    short_digits[70] = 'Seventy'
    short_digits[80] = 'Eighty'
    short_digits[90] = 'Ninety'
    
    short_digits[100] = 'OneHundred'
    short_digits[200] = 'TwoHundred'
    short_digits[300] = 'ThreeHundred'
    short_digits[400] = 'FourHundred'
    short_digits[500] = 'FiveHundred'
    short_digits[600] = 'SixHundred'
    short_digits[700] = 'SevenHundred'
    short_digits[800] = 'EightHundred'
    short_digits[900] = 'NineHundred'
    
    result = []
    
