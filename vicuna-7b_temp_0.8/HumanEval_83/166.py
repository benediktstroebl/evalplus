
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base cases
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        # if n is odd, it has at least one digit of 1, so we increment the count
        # twice for the ends
        count = 1
        for i in range(2, n-1):
            count += (n-i)/2
        # if n is even, it has at least one digit of 1, so we increment the count
        # once for the end
        count += (n-1)/2
        return count
