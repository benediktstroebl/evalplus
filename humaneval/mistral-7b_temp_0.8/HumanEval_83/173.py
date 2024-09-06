
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_of_1_starts = 0
    num_of_1_ends = 0
    for i in range(1, n):
        if i == 1:
            num_of_1_starts += 1
        elif n - i == 1:
            num_of_1_ends += 1
    num_of_1_starts += 1
    return num_of_1_starts + num_of_1_ends

