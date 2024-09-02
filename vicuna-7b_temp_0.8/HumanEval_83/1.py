
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Number of single digit numbers
    num_ones = 0

    # Number of n-digit numbers that start with 1
    num_starts = 0

    # Number of n-digit numbers that end with 1
    num_ends = 0

    for i in range(2, n+1):
        # Count the number of n-digit numbers that start with 1
        if i % 2 == 0:
            num_starts += num_starts // i
        else:
            num_starts += num_ones

        # Count the number of n-digit numbers that end with 1
        if i % 2 == 0:
            num_ends += num_ends // i
        else:
            num_ends += num_ones

        num_ones += i

    return num_starts + num_ends

print(starts_one_ends(1000))
