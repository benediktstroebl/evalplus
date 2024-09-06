
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if n is even, in which case all digits are even
    if n % 2 == 0:
        return 0

    # Check if n is odd, in which case it has an odd digit
    odd = n % 2

    # Initialize result to 1
    result = 1

    # Loop through digits, increasing the result for odd digits and decreasing
    # for even digits
    for i in range(1, len(str(n))):
        if n[i] % 2 == odd:
            result *= n[i]
        else:
            result *= n[i] / 2

    return result
