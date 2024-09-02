
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n < 0 or not n % 10 in [1, 3, 5, 7, 9]:
        return 0
    digit_list = [int(n % 10) for _ in range(len(str(n)))[::-1]]
    digit_product = 1
    for i in reversed(range(len(digit_list))):
        digit_product *= int(digit_list[i])
    return digit_product
