
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n -= 1
    digit_n = 1
    while n > 0:
        digit_n *= 10
        n -= 1
    one_cnt = digit_n / 10
    n_digit_ones = 0
    for i in range(10):
        if i == 1:
            n_digit_ones += one_cnt
        n_digit_ones += i * digit_n
    return n_digit_ones
