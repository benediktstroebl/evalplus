
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

    if not arr: return []
    
    num_list = [str(num) for num in arr]
    
    length = len(num_list)
    
    for i in range(length-1):
        for j in range(i, length):
            if num_list[i][0] <= num_list[j][0] <= num_list[i][0]+9:
                num_list[i], num_list[j] = num_list[j], num_list[i]
            elif num_list[i][0]+9 < num_list[j][0]:
                break
    
    return [digit_name(num) for num in num_list]
        
