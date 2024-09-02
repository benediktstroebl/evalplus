
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num_str = str(n)
    product = 1
    for i in range(len(num_str)):
        digit = num_str[i]
        if digit.isdigit() and int(digit) % 2 == 1:
            product *= int(digit)
    return product

