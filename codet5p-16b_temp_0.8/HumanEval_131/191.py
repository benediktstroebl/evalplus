
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n <= 0:
        return 0
    else:
        i = 1
        n = int(n)
        while n >= i:
            if n % i == 0:
                if i % 2 == 0:
                    i = i + 1
                else:
                    return 0
            else:
                i = i + 1
        return i
