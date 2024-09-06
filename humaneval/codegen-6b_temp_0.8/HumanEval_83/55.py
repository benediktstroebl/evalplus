
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def starts_one_ends_helper(n, count):
        if n == 1:
            count[1] += 1
            return
        starts_one_ends_helper(n - 1, count)
        count[n] += count[n - 1]
    count = defaultdict(int)
    starts_one_ends_helper(n, count)
    return count[n]
