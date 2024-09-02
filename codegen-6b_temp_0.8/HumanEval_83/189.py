
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Time: O(n), Space: O(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    num_digits = n
    count = 0
    total = 0
    for i in range(10, n + 1):
        if i % 10 == 1:
            count += n
        elif i % 10 == 0:
            total += (i // 10) * n
    return total + count

assert starts_one_ends(0) == 0
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 2
assert starts_one_ends(3) == 5
assert starts_one_ends(4) == 11
assert starts_one_ends(5) == 22
assert starts_one_ends(6) == 43
assert starts_one_ends(7) == 59
assert starts_one_ends(8) == 90
assert starts_one_ends(9) == 103
assert starts_one_ends(10) == 124
assert starts_one_ends(11) == 149
assert starts_one_ends(12) == 164
assert starts_one_ends(13) == 181
assert starts_one_ends(14) == 202
assert starts_one_ends(15) == 223
assert starts_one_ends(16) == 241

