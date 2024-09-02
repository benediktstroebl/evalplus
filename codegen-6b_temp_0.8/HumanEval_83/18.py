
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if len(str(n)) == 1:
        return 0
    else:
        # Every multiple of 10 in range 1 to n - 1
        #   is a multiple of 100
        # Every multiple of 10 in range n - 1 to n
        #   is a multiple of 1000
        return len([i for i in range(1, n) if i % 10 == 0 or i % 100 == 0 or i % 1000 == 0])

