
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in xrange(10**(n-1), 10**n):
        if str(i).startswith('1') or str(i).endswith('1'):
            ans += 1
    return ans

assert starts_one_ends(3) == 10
assert starts_one_ends(7) == 49
assert starts_one_ends(15) == 9
assert starts_one_ends(23) == 25

