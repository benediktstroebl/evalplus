
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # Your code here
    # if x < 0 or y < 0 or x > y:
    #     return -1
    # for num in range(x, y + 1):
    #     if num % 2 == 0:
    #         return num
    # return -1
    #return -1 if (x < 0 or y < 0 or x > y) else max(filter(lambda x: x % 2 == 0, range(x, y + 1)), default = -1)
    return max((n for n in range(x, y + 1) if n % 2 == 0), default = -1)
