
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_starting_one = num_ending_one = 0

    # 3-digit numbers
    if n >= 3:
        num_starting_one = 10 ** (n - 1)
        num_ending_one = 9 * (10 ** (n - 2))

    # 2-digit numbers
    if n == 2:
        num_starting_one = 10 ** 1
        num_ending_one = 9 * (10 ** 0)

    # 1-digit numbers
    if n == 1:
        num_starting_one = 1
        num_ending_one = 1

    return num_starting_one + num_ending_one

