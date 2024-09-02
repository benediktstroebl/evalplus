
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The function uses the following recurrence:
    # T(n) = 0 if n = 0
    # T(n) = 1 if n = 1
    # T(n) = 1 if n = 2
    # T(n) = 2 if n = 3
    # T(n) = 4 if n = 4
    # T(n) = 7 if n = 5
    # T(n) = T(n-1) + T(n-2) if n >= 6
    # The base case is n=0, which does not contribute to the count
    # The next case is n=1, which contributes 1 to the count, since
    # 1 is the only n-digit positive integer that starts with 1.
    # The case n=2 is the same as n=1, so we can skip it.
    # The case n=3 is also the same as n=1, so we can skip it.
    # The case n=4 is the same as n=1, so we can skip it.
    # The case n=5 is the same as n=1, but we need to add the contribution
    # of 2 (which is the only n-digit positive integer that ends with 1).
    # The general case is n>=6, which is the same as n-1>=5, which is
    # the same as n-2>=4, which is the same as n-3>=3, which is the same
    # as n-4>=2. So we can simplify the recurrence to T(n) = T(n-1) + T(n-2).
    return 1 + T(n-1) + T(n-2)
