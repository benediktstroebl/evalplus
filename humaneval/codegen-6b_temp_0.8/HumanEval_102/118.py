
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    nums = range(max(x, y), min(x, y) + 1)
    n = len(nums)
    for i in range(n):
        if nums[i] % 2 == 0 and nums[i] >= x and nums[i] <= y:
            return nums[i]
    return -1
