
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def digit_sum(n):
        return sum(int(i) for i in str(n))
    return sum(digit_sum(i) == 1 or digit_sum(i) == n for i in range(1, n))
