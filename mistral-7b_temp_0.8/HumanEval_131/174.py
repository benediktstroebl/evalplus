
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n:
        return 0
    digits_list = []
    while n > 0:
        digit = n % 10
        n //= 10
        if digit % 2:
            digits_list.append(digit)
    return reduce(lambda x, y: x * y, digits_list) or 0
