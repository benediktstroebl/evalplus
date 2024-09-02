
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return len([i for i in range(1, n+1) if i == int('1'*i) or i == int('9'*i)])



assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 2
assert starts_one_ends(3) == 4
assert starts_one_ends(4) == 10
assert starts_one_ends(5) == 30
assert starts_one_ends(6) == 112
assert starts_one_ends(7) == 228

