
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2 if x > 0 else 0, n)) == 0:
        return 0
    # Check if all digits are odd
    if sum(map(lambda x: x % 2 if x > 0 else 1, n)) == len(str(n)) * 2:
        return sum(int(digit) ** 2 for digit in str(n))
    # Check if there is at least one odd digit
    odd_digits = [int(digit) for digit in str(n)[1:-1]]
    if len(odd_digits) == 0:
        return 0
    # The result is the product of the odd digits
    result = 1
    for digit in odd_digits:
        result *= digit
    return result
