
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # number of 1-digit integers ending with 1
    count = 9

    # number of 2-digit integers ending with 1
    count += 8*9

    # number of 3-digit integers ending with 1
    count += 7*8*9

    # ...

    # number of n-digit integers ending with 1
    count += 1*2*3*...*(9 - n + 1)

    # number of 1-digit integers starting with 1
    count += 9

    # number of 2-digit integers starting with 1
    count += 8*9

    # ...

    # number of n-digit integers starting with 1
    count += 1*2*3*...*(9 - n + 1)

    return count
