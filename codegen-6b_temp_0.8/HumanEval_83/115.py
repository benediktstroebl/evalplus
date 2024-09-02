
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    from itertools import count

    def helper(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * helper(n-1)

    return sum(helper(n) for n in count())

