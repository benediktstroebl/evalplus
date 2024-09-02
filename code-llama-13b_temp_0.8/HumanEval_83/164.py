
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n is 1, there are two possibilities
    if n == 1:
        return 2

    # if n is 2, there is only one possibility
    if n == 2:
        return 1

    # if n is greater than 2, there is one possibility if n ends in 1
    if n % 10 == 1:
        return 1

    # if n is greater than 2, there is one possibility if n starts with 1
    if n / 10 == 1:
        return 1

    # if n is greater than 2 and n does not end in 1 and does not start with 1,
    # the answer is zero
    return 0

