
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    ones_last_digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for last_digit in ones_last_digit:
        if last_digit == 1:
            count += 1
        else:
            count += 10 ** (n - 1)
    return count
