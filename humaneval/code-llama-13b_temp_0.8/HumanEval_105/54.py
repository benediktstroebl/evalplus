
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
    ################## 
    # Step 1: get the number of each digit
    # use counter class to count the numbers
    # Step 2: sort the dictionary by value (descending)
    # Step 3: reverse the dictionary
    # Step 4: get the key corresponding to the value of the dictionary
    # Step 5: return the list of numbers
    #######################
    numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    if len(arr) == 0:
      return []
    dic = {}
    for i in range(len(arr)):
      if arr[i] >=1 and arr[i] <= 9:
        if str(arr[i]) not in dic:
          dic[str(arr[i])] = 1
        else:
          dic[str(arr[i])] += 1
      else:
        if 'other' not in dic:
          dic['other'] = 1
        else:
          dic['other'] += 1
    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    reverse_dic = list(reversed(sort_dic))
    return_dic = [numbers[int(x[0])-1] for x in reverse_dic if x[0] != 'other']
    return return_dic

