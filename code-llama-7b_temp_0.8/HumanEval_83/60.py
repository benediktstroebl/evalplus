
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    count = 0
    one = "1"
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i + j + k + 1 == n and int(one + str(i) + str(j) + str(k)) > 0:
                    count += 1
    return count

