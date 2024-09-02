
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count = 0
    # for i in range(0, n):
    #     if i < 10:
    #         count += 1
    #     else:
    #         if i % 10 == 1 or i % 10 == 9:
    #             count += 1
    # return count
    # count = 0
    # for i in range(10 ** (n - 1), 10 ** n):
    #     if i % 10 == 1 or i % 10 == 9:
    #         count += 1
    # return count
    return sum(i // 10 for i in range(10 ** (n - 1), 10 ** n) if i % 10 in [1, 9])

