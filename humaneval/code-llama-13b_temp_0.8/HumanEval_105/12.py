
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
    if not arr:
        return arr
    
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    
    for num in arr:
        if num > 0 and num <= 9:
            if num == 1:
                one.append(num)
            elif num == 2:
                two.append(num)
            elif num == 3:
                three.append(num)
            elif num == 4:
                four.append(num)
            elif num == 5:
                five.append(num)
            elif num == 6:
                six.append(num)
            elif num == 7:
                seven.append(num)
            elif num == 8:
                eight.append(num)
            elif num == 9:
                nine.append(num)
    
    one = one[::-1]
    two = two[::-1]
    three = three[::-1]
    four = four[::-1]
    five = five[::-1]
    six = six[::-1]
    seven = seven[::-1]
    eight = eight[::-1]
    nine = nine[::-1]
    
    ret = []
    
    for item in one:
        ret.append("One")
    for item in two:
        ret.append("Two")
    for item in three:
        ret.append("Three")
    for item in four:
        ret.append("Four")
    for item in five:
        ret.append("Five")
    for item in six:
        ret.append("Six")
    for item in seven:
        ret.append("Seven")
    for item in eight:
        ret.append("Eight")
    for item in nine:
        ret.append("Nine")
    
    return ret

