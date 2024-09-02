
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # get n-digit numbers that start or end with 1
    if n == 1:
        return 10

    count = 0

    # first check the first digit
    # one starts, one ends
    for i in range(10):
        count += starts_one_ends(i) * 9

    # check the last digit
    count += starts_one_ends(n - 1)

    # check the middle digits
    for i in range(1, n):
        count += (10 ** (n - i - 1)) * (9 - 10 ** (i - 1))

    # print(count)
    return count


assert starts_one_ends(1) == 10
assert starts_one_ends(2) == 55
assert starts_one_ends(3) == 165
assert starts_one_ends(4) == 385
assert starts_one_ends(5) == 732
assert starts_one_ends(6) == 1101
assert starts_one_ends(7) == 1350
assert starts_one_ends(8) == 1588
assert starts_one_ends(9) == 1628
assert starts_one_ends(10) == 1628
assert starts_one_ends(11) == 1799
assert starts_one_ends(12) == 1905
assert starts_one_ends(13) == 2009
assert starts_one_ends(14) == 2438
assert starts_one_ends(15) == 2438
assert starts_one_ends(16) == 2801
assert starts_one_ends(17) == 2947
assert starts_one_ends(18) == 3059
assert starts_one_ends(19) == 3264
assert starts_one_ends(20) == 3328
assert starts_one_ends(21) == 3392
assert starts_one_ends(22) == 3508
assert starts_one_ends(23) == 3588
assert starts_one_ends(24) == 3663
assert starts_one_ends(25) == 3769
assert starts_one_ends(26) == 3792
assert starts_one_ends(27) == 3879
assert starts_one_ends(28) == 4033
assert starts_one_ends(29)