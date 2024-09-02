
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    def is_odd(n):
        return n % 2 == 1

    if n < 1:
        return 0
    digit_list = []
    while n > 0:
        digit_list.append(n % 10)
        n //= 10
    digit_list = list(filter(is_odd, digit_list))
    if not digit_list:
        return 0
    return reduce(lambda x, y: x * y, digit_list)

