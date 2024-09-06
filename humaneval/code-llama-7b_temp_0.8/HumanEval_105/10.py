
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
    str_arr = []
    arr_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in arr:
        if num > 0 and num < 10:
            str_arr.append(num)
    
    print(str_arr)
    #sorted_arr = str_arr.sort()
    sorted_arr = sorted(str_arr)
    print(sorted_arr)
    #return str_arr
    #return sorted_arr
    
    reverse_arr = sorted_arr.reverse()
    print(reverse_arr)
    #return reverse_arr
    
    stringify_arr = str(reverse_arr)
    print(stringify_arr)
    #return stringify_arr
    
    string_arr = []
    for num in stringify_arr:
        if num == "1":
            string_arr.append("One")
        elif num == "2":
            string_arr.append("Two")
        elif num == "3":
            string_arr.append("Three")
        elif num == "4":
            string_arr.append("Four")
        elif num == "5":
            string_arr.append("Five")
        elif num == "6":
            string_arr.append("Six")
        elif num == "7":
            string_arr.append("Seven")
        elif num == "8":
            string_arr.append("Eight")
        elif num == "9":
            string_arr.append("Nine")
    
    return string_arr
    
