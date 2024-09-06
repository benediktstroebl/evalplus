
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10**n):
        if (i // 10**(n-1) == 1):
            count += 1
        if (i % 10**(n-1) == 9):
            count += 1
    return count
assert starts_one_ends(3) == 9
assert starts_one_ends(2) == 16
assert starts_one_ends(1) == 81
assert starts_one_ends(5) == 252
assert starts_one_ends(7) == 1020
assert starts_one_ends(9) == 744
assert starts_one_ends(10) == 1224
assert starts_one_ends(11) == 729
assert starts_one_ends(12) == 1512
assert starts_one_ends(13) == 3128
assert starts_one_ends(14) == 8964
assert starts_one_ends(15) == 9592
assert starts_one_ends(16) == 10240
assert starts_one_ends(17) == 75568
assert starts_one_ends(18) == 165984
assert starts_one_ends(19) == 959056
assert starts_one_ends(20) == ...
