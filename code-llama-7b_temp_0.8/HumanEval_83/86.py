
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_start_ones = num_end_ones = 0
    for n in range(10 ** (n - 1), 10 ** n):
        if n % 10 == 1 or n // 10 ** (n - 1) % 10 == 1:
            num_start_ones += 1
        elif n % 10 == 9 or n // 10 ** (n - 1) % 10 == 9:
            num_end_ones += 1
    return num_start_ones + num_end_ones

