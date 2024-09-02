
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    digits = [str(i) for i in range(1, n + 1)]
    starts = len(digits) - digits.index('1')
    ends = len(digits) - digits.index('1') - 1
    return starts + ends
