
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0

    start = 1
    end = 10
    result = 0

    while start <= (n - 1):
        result += n - start + 1
        start *= 10
    while end >= 10:
        result += n - end + 1
        end /= 10

    return result

assert starts_one_ends(1) == 0
assert starts_one_ends(2) == 1
assert starts_one_ends(3) == 2
assert starts_one_ends(5) == 4
