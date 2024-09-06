
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n = str(n)
    first = int(n[0])
    last = int(n[-1])
    if first == last == 1:
        return 2
    elif first == 1:
        return 2
    elif last == 1:
        return 2
    else:
        return 1
