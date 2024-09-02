
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def c(n):
        """
        Counts the number of integers of length n that start or end with 1
        """
        if n == 1:
            return 1
        return 0
    count = 0
    for i in range(1, 10):
        count += c(i)
        count += c(10 - i)
    return count


assert starts_one_ends(1) == 10

