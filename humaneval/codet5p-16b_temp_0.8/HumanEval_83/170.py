
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    digits = [0] * n
    ones = 0
    for d in range(1, 10):
        digits[0] = d
        if d == 1:
            ones += 1
        for i in range(1, n):
            digits[i] = digits[i-1]
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
            if digits[i] == 1:
                ones += 1
    return ones
