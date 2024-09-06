
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
    nine_index = 0
    for n in arr:
        if n > 9:
            arr[nine_index] = n
            nine_index += 1
        elif n < 0:
            continue
        else:
            arr[nine_index] = n
            nine_index += 1
    if nine_index == 0:
        return []
    elif nine_index == 1:
        return [ONE[arr[0]]]
    elif nine_index == 2:
        return [ONE[arr[0]], TWO[arr[1]]]
    elif nine_index == 3:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]]]
    elif nine_index == 4:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]]]
    elif nine_index == 5:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]], FIVE[arr[4]]]
    elif nine_index == 6:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]], FIVE[arr[4]], SIX[arr[5]]]
    elif nine_index == 7:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]], FIVE[arr[4]], SIX[arr[5]], SEVEN[arr[6]]]
    elif nine_index == 8:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]], FIVE[arr[4]], SIX[arr[5]], SEVEN[arr[6]], EIGHT[arr[7]]]
    elif nine_index == 9:
        return [ONE[arr[0]], TWO[arr[1]], THREE[arr[2]], FOUR[arr[3]], FIVE[arr[4]], SIX[arr[5]], SEVEN[arr[6]], EIGHT[arr[7]], NINE[arr[8]]]
