
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
    
    # convert array to string
    string = ""
    for num in arr:
        string += str(num)
    
    # convert string to number
    num = int(string)
    
    # reverse number
    num = int(str(num)[::-1])
    
    # convert number to string
    string = str(num)
    
    # convert string to array
    arr = [int(i) for i in string]
    
    # put string in correct order
    arr.sort(reverse = True)
    
    # convert array to string
    string = ""
    for num in arr:
        string += str(num)
    
    # string to names
    string = string.replace('1', 'one').replace('2', 'two').replace('3', 'three').replace('4', 'four').replace('5', 'five').replace('6', 'six').replace('7', 'seven').replace('8', 'eight').replace('9', 'nine').replace('0', 'zero')
    
    # string to array
    arr = string.split()
    
    return arr
