
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_ones = 0
    end_ones = 0

    for n in range(n):
        if n % 10 == 1:
            start_ones += 1
        if n // 10 == 1:
            end_ones += 1

    return start_ones + end_ones
