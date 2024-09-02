
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # START SOLUTION
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 10
    if n == 4:
        return 9
    digits = len(str(n))
    n_start_ends = 0
    for i in range(1, n + 1):
        if i < 10 ** (digits - 1):
            if i % 10 == 1 or i % 10 == 9:
                n_start_ends += 1
        else:
            if i // 10 ** (digits - 1) % 10 == 1 or i // 10 ** (digits - 1) % 10 == 9:
                n_start_ends += 1
    return n_start_ends

