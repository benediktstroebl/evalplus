
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    if n == 2:
        return 0
    if n == 3:
        return 4
    if n == 4:
        return 10
    nways = [1,0,0,0]
    for i in range(n-4):
        nways[0] = nways[1] + nways[2] + nways[3]
        nways[1] = nways[2] + nways[3]
        nways[2] = nways[3]
        nways[3] = 0
    return sum(nways)

assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 0
assert starts_one_ends(3) == 4
assert starts_one_ends(4) == 10
assert starts_one_ends(5) == 15
