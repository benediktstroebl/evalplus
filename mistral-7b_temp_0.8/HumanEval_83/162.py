
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_digit = 1
    end_digit = 1

    if n == 1:
        return 1
    elif n == 2:
        return 4
    else:
        total = 0
        for x in range(1, 10 ** (n - 1)):
            total += 1 + (10 ** (n - 2))
        return total

