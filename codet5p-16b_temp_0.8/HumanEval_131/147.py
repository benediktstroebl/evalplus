
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = [int(digit) for digit in str(n)]
    odd_digits_list = [digit for index, digit in enumerate(digits_list) if index % 2 == 1]
    return sum(odd_digits_list)
