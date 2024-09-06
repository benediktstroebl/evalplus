
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    for i in range(1, n + 1):
        if int(str(i)[0]) == 1 or int(str(i)[-1]) == 1:
            count += 1

    return count


assert starts_one_ends(3) == 8
assert starts_one_ends(2) == 5

