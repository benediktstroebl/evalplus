
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert n to a string and reverse it
    n_str = str(n)[::-1]

    # Split the string into odd and even digits
    odd_digits = n_str[1::2]
    even_digits = n_str[0]

    # Check if all digits are even
    if all(c in '0' for c in even_digits):
        return 0

    # Combine the odd and even digits to form the product
    product = 0
    for digit in odd_digits:
        product *= digit
    product *= even_digits[0]

    return product
