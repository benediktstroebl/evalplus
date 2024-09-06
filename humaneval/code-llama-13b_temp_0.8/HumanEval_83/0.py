
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if len(str(n)) < 2:
        return 0

    count = 0
    for i in range(10 ** (len(str(n)) - 2)):
        # Add beginning 1 count
        if i == 0:
            count += 1

        # Add ending 1 count
        if i == 9 ** (len(str(n)) - 2):
            count += 1

    return count

