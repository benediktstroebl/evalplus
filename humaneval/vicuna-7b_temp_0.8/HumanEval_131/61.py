
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case
    if n < 2:
        return n
    # convert to string
    n = str(n)
    # split string into odd and even digits
    odd_digits = [int(d) if d.isdigit() else 0 for d in n]
    even_digits = [int(d) if d.isdigit() else 0 for d in n[::2]]
    # multiply odd digits
    product = 1
    for i in range(1, len(odd_digits)):
        product *= odd_digits[i]
    # return product
    return product
