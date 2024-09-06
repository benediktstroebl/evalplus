
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    def is_even(num):
        """
        Return if the number is even or not.
        """
        return num % 2 == 0

    def get_next(num):
        """
        Return the next number.
        """
        return num + 1

    def get_prev(num):
        """
        Return the previous number.
        """
        return num - 1

    if x > y or x < 1 or y > 1000 or y < 1:
        return -1

    # The number to return.
    res = -1

    # The current number.
    num = x

    while num <= y:
        if is_even(num):
            res = num
            break

        # The next number.
        num = get_next(num)

    return res
