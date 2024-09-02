
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    answer = 1

    for i in xrange(len(str(n))):
        if int(str(n)[i]) % 2 != 0:
            answer *= int(str(n)[i])
    return answer

