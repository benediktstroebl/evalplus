
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
    else:
        sort_num = sorted(arr)
        sort_num = [int(x) for x in sort_num]
        result = []
        i = 0
        while i < len(sort_num):
            if sort_num[i] == 1:
                result.insert(0, "One")
                i += 1
            elif sort_num[i] == 2:
                result.insert(0, "Two")
                i += 1
            elif sort_num[i] == 3:
                result.insert(0, "Three")
                i += 1
            elif sort_num[i] == 4:
                result.insert(0, "Four")
                i += 1
            elif sort_num[i] == 5:
                result.insert(0, "Five")
                i += 1
            elif sort_num[i] == 6:
                result.insert(0, "Six")
                i += 1
            elif sort_num[i] == 7:
                result.insert(0, "Seven")
                i += 1
            elif sort_num[i] == 8:
                result.insert(0, "Eight")
                i += 1
            elif sort_num[i] == 9:
                result.insert(0, "Nine")
                i += 1
            else:
                result.insert(0, str(sort_num[i]))
                i += 1
        return result

arr = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(arr)) 
