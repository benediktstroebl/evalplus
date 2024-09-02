
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def digits(n):
        even = []
        odd = []
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)
            n = n // 10
        if len(odd) == 0:
            return 0
        return reduce(lambda x, y: x * y, odd)


    return 0
