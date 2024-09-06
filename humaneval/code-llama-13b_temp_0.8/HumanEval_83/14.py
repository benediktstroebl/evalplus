
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # set the counters
    count = 0
    count_start = 0
    count_end = 0

    # check the end of the number
    if (n%10) == 1:
        count_end = count_end + 1

    # check the start of the number
    if (n//10) == 1:
        count_start = count_start + 1

    count = count + count_end + count_start

    return count

