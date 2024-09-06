
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_products = 1

    # You need to split your number in separate digits
    for digit in str(n):
        if int(digit) % 2 != 0:
            odd_products *= int(digit)

    return odd_products
