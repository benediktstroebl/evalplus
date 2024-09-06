
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    s = 0
    for i in range(1, n+1):
        if i > 10:
            for j in range(10, i+1):
                if j % 10 == 1:
                    s += 1
        else:
            if i % 10 == 1:
                s += 1
    return s
