
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    m = len(str(n))
    if m == 1:
        return 0
    elif m == 2:
        return (n - 1) * (n + 1) // 2
    elif m == 3:
        return (n - 1) * (n + 1) * (n + 2) // 6
    elif m == 4:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) // 24
    elif m == 5:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) * (n + 4) // 120
    elif m == 6:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5) // 720
    elif m == 7:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5) * (n + 6) // 5040
    elif m == 8:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5) * (n + 6) * (n + 7) // 40320
    elif m == 9:
        return (n - 1) * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5) * (n + 6) * (n + 7) * (n + 8) // 362880
    else:
        return 0

