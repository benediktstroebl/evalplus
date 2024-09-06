
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = []
    while n:
        digits_list.append(n % 10)
        n //= 10
    digits_list.reverse()
    product = 1
    for digit in digits_list:
        if digit % 2:
            product *= digit
    return product
