
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    a_count = 0
    b_count = 0
    for i in range(1, n+1):
        count = 0
        for j in str(i):
            if int(j) == 1:
                count += 1
        if count == 1:
            a_count += 1
        if count == n:
            b_count += 1
    return [a_count, b_count]

