
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    # initialize the answer
    ans = -1

    # initialize the biggest integer
    i = y

    # loop over the integers from y to x (inclusive)
    while i >= x:

        # if the integer is even and it is bigger than ans, set ans to i
        if i % 2 == 0 and i > ans:
            ans = i

        # decrement i
        i -= 1

    # return the answer
    return ans

