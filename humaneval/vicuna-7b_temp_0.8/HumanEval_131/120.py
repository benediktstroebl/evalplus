
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0

    # Find the first odd digit
    digits = map(int, str(n))
    for i, d in enumerate(digits):
        if d % 2 != 0:
            break
    else:
        return 0

    # Find the number of odd digits
    odd_count = 1
    for i in reversed(range(len(digits) - 1)):
        if digits[i] % 2 != 0:
            odd_count += 1

    # Multiply the odd digits
    return odd_count * (2 ** (len(digits) - odd_count))
