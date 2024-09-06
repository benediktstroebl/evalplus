
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    #  The given input is in the range [x, y].
    if x < y:
        #  Create a list of numbers in the range [x, y] inclusive
        nums = range(x, y + 1)
        #  Create a list of numbers that are in the range [x, y] inclusive
        #  and are divisible by 2
        choices = [num for num in nums if num % 2 == 0]
        #  Return the biggest number in the list
        return max(choices)
    else:
        return -1

