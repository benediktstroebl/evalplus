
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def is_one(num):
        return num == 1

    def count_ends(num):
        result = 0
        while num > 0:
            num //= 10
            result += 1
        return result

    result = 0
    for i in range(1, n):
        if is_one(i):
            result += (n - count_ends(i)) * 9 ** (n - count_ends(i) - 1)
        else:
            result += 10 ** (n - count_ends(i) - 1) - 1
    return result

