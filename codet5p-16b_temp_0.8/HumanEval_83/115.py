
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    starts = 0
    ends = 0

    for i in range(10 ** (n-1), 10 ** n):
        if i % 10 == 1:
            starts += 1
            if n % 2 == 1:
                ends += 1
        if i % 10 == 9:
            ends += 1
            if n % 2 == 1:
                starts += 1

    return starts + ends
