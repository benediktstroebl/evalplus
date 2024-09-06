
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10):
        # 10^(n - 1) 1's in the integer
        digit_count = 10 ** (n - 1)
        # if 10^(n - 1) + 9^(n - 1) 1's in the integer
        # if 10 ** n + 9 ** n 1's in the integer
        digit_count *= 10
        # if 10 ** n + 9 ** n 1's in the integer + 9 ** n 9's in the integer
        digit_count += 9 * (10 ** n)

        count += digit_count
    return count
