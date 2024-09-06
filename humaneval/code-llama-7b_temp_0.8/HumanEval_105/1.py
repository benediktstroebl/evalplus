
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
    # print(arr)
    arr = list(filter(lambda x: 1 <= x <= 9, arr))
    arr.sort(reverse=True)
    # print(arr)
    one_two_three = ["One", "Two", "Three"]
    four_five_six = ["Four", "Five", "Six"]
    seven_eight_nine = ["Seven", "Eight", "Nine"]
    new_arr = []
    for x in arr:
        if x == 1:
            new_arr.append(one_two_three[0])
        elif x == 2:
            new_arr.append(one_two_three[1])
        elif x == 3:
            new_arr.append(one_two_three[2])
        elif x == 4:
            new_arr.append(four_five_six[0])
        elif x == 5:
            new_arr.append(four_five_six[1])
        elif x == 6:
            new_arr.append(four_five_six[2])
        elif x == 7:
            new_arr.append(seven_eight_nine[0])
        elif x == 8:
            new_arr.append(seven_eight_nine[1])
        elif x == 9:
            new_arr.append(seven_eight_nine[2])
        else:
            pass
    return new_arr

