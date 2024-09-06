
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if (n % 2) == 0:
        return 0
    digits = [int(n) % 10]
    while (len(digits) > 0):
        digits = digits[1:]
        for i in xrange(1, len(digits)):
            if (digits[i] % 2 != digits[i-1] % 2):
                break
        else:
            product = int(digits[0])
            for i in xrange(1, len(digits)):
                digits[i] = int(digits[i]) // 2
            digits = digits[i+1:]
            return product
