
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def count(num):
        cnt = 0
        while num:
            cnt += 1
            num //= 10
        return cnt

    n = count(n)
    return sum([1 for i in [2, 3, 4, 5, 6, 7] if cnt(i) == n])

