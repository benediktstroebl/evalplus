
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ans = 0
    for i in range(1, 10):
        ans += starts_one_ends_helper(n, str(i))
    return ans


assert starts_one_ends(2) == 3
assert starts_one_ends(3) == 8
assert starts_one_ends(4) == 10
assert starts_one_ends(5) == 15
assert starts_one_ends(6) == 25
assert starts_one_ends(7) == 42
assert starts_one_ends(8) == 78
assert starts_one_ends(9) == 108

assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 2
assert starts_one_ends(3) == 3
assert starts_one_ends(4) == 6
assert starts_one_ends(5) == 10
assert starts_one_ends(6) == 15
assert starts_one_ends(7) == 21
assert starts_one_ends(8) == 28
assert starts_one_ends(9) == 36

assert starts_one_ends(0) == 0

