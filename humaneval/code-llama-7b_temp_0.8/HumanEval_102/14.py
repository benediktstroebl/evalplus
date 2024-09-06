
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if (x%2 == 0):
        min_num = x
    else:
        min_num = x + 1

    max_num = y
    if (y%2 == 0):
        max_num = y
    else:
        max_num = y - 1

    nums = []
    for num in range(min_num, max_num + 1, 2):
        nums.append(num)
    
    if (len(nums) > 0):
        return max(nums)
    else:
        return -1
