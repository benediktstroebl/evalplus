
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

    def replace_str(str_num):
        if str_num == '1':
            return 'One'
        elif str_num == '2':
            return 'Two'
        elif str_num == '3':
            return 'Three'
        elif str_num == '4':
            return 'Four'
        elif str_num == '5':
            return 'Five'
        elif str_num == '6':
            return 'Six'
        elif str_num == '7':
            return 'Seven'
        elif str_num == '8':
            return 'Eight'
        elif str_num == '9':
            return 'Nine'

    result = []
    sorted_arr = [i for i in arr if i in range(1, 10)]
    sorted_arr.sort()
    sorted_arr.reverse()
    for i in sorted_arr:
        result.append(replace_str(str(i)))
    return result

