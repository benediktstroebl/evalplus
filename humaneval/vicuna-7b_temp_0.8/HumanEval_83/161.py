
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If n is 1, it's the first digit, so return 1.
    if n == 1:
        return 1
    # If n is 2, it doesn't end with 1, so return 0.
    elif n == 2:
        return 0
    # If n is 3, it ends with 1, so return 1.
    elif n == 3:
        return 1
    # If n is greater than 3, it's neither the first nor the last digit,
    # so we need to count the number of n-1 digit numbers that start with 1
    # and the number of n-1 digit numbers that end with 1.
    else:
        # Count the number of n-1 digit numbers that start with 1.
        count_start = 0
        for i in range(2, n):
            if i * (i + 1) < n:
                count_start += (n - i + 1) // i
        # Count the number of n-1 digit numbers that end with 1.
        count_end = 0
        for i in reversed(range(2, n)):
            if i * (i + 1) < n:
                count_end += (n - i + 1) // i
        # Return the sum of the two counts.
        return count_start + count_end
