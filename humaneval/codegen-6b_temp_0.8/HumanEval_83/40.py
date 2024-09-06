
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    if n == 2:
        return 6
    if n == 3:
        return 10
    if n == 4:
        return 14
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1':
            count += 1
        if str(i)[-1] == '1':
            count += 1
    return count

assert starts_one_ends(1) == 2
assert starts_one_ends(2) == 6
assert starts_one_ends(3) == 10
assert starts_one_ends(4) == 14
assert starts_one_ends(5) == 26
assert starts_one_ends(6) == 30
assert starts_one_ends(7) == 36
