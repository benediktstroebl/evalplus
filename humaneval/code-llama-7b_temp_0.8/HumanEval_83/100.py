
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 10
    elif n == 2:
        return 9 * 10 + 1
    elif n == 3:
        return 9 * 10 + 1 + 9

    numbers = ['1' + '0' * (n - 1)]
    for i in range(1, n - 1):
        numbers.append('0' * (n - i) + '1' + '0' * (i - 1))
    numbers.append('0' * (n - 1) + '1')
    return 2 * sum(map(len, numbers))
