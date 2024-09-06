
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
    length_order = []
    for num in arr:
        if num in range(1, 10):
            length_order.append(num)
    length_order.sort()
    length_order.reverse()
    length_order_str = [str(i) for i in length_order]
    length_order_str = ''.join(length_order_str)
    return length_order_str
    # if len(length_order_str) == 0:
    #     return []
    # elif len(length_order_str) == 1:
    #     return [length_order_str]
    # elif len(length_order_str) == 2:
    #     return [length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 3:
    #     return [length_order_str[2], length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 4:
    #     return [length_order_str[3], length_order_str[2], length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 5:
    #     return [length_order_str[4], length_order_str[3], length_order_str[2], length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 6:
    #     return [length_order_str[5], length_order_str[4], length_order_str[3], length_order_str[2], length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 7:
    #     return [length_order_str[6], length_order_str[5], length_order_str[4], length_order_str[3], length_order_str[2], length_order_str[1], length_order_str[0]]
    # elif len(length_order_str) == 8:
