
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def d(n):
        if n == 0:
            return 1
        return d(n-1)+1
    
    def k(n):
        if n == 0:
            return 1
        return k(n-1)*d(n)
    
    if n == 0:
        return 1
    return k(n-1)
