
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if not isinstance(x, int) or not isinstance(y, int):
        return -1

    if x % 2 != 0 or y % 2 != 0:
        return -1
    elif x < 0 or y < 0:
        return -1
    elif x > y:
        return -1
    else:
        nums = []

        if (x % 2 == 0):
            nums.append(x)
        if (y % 2 == 0):
            nums.append(y)

        nums.sort()
        return nums[len(nums)-1]

