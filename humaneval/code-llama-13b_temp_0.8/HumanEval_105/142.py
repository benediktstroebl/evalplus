
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
    # your code here

    str_lst = []
    for num in arr:
        if 1 <= num <= 9:
            str_lst.append(str(num))
        else:
            str_lst.append(str(num))
    
    str_lst.sort()
    str_lst.reverse()

    for idx, num in enumerate(str_lst):
        if num == '1':
            str_lst[idx] = 'One'
        elif num == '2':
            str_lst[idx] = 'Two'
        elif num == '3':
            str_lst[idx] = 'Three'
        elif num == '4':
            str_lst[idx] = 'Four'
        elif num == '5':
            str_lst[idx] = 'Five'
        elif num == '6':
            str_lst[idx] = 'Six'
        elif num == '7':
            str_lst[idx] = 'Seven'
        elif num == '8':
            str_lst[idx] = 'Eight'
        elif num == '9':
            str_lst[idx] = 'Nine'
    
    return str_lst
