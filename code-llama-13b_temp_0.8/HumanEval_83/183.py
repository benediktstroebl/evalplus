
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2

    count = 0
    one_digits = [1] * n
    start_one = int("1" + "0" * (n - 1))
    end_one = int("1" + "0" * (n - 2))
    for i in range(start_one, 10 ** n):
        if i % (10 ** (n - 1)) == end_one:
            count += 1
    return count + 2
