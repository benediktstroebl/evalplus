
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digit_list = []
    while n >= 1:
        digit_list.append(n % 10)
        n //= 10
    return reduce(lambda x, y: x * y, digit_list)
