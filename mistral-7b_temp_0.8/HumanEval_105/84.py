
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
    # arr = [2, 1, 1, 4, 5, 8, 2, 3]
    # arr = [1, -1 , 55]
    arr = []
    num_list = [x for x in range(1, 10)]
    num_dict = {}
    for i in num_list:
        num_dict[i] = i
    num_dict[10] = "Ten"
    num_dict[11] = "Eleven"
    num_dict[12] = "Twelve"
    num_dict[13] = "Thirteen"
    num_dict[14] = "Fourteen"
    num_dict[15] = "Fifteen"
    num_dict[16] = "Sixteen"
    num_dict[17] = "Seventeen"
    num_dict[18] = "Eighteen"
    num_dict[19] = "Nineteen"
    num_dict[20] = "Twenty"
    
