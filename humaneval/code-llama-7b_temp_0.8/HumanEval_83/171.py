
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    cnt = 0

    # First count the numbers that start with 1
    if n >= 1:
        # Add n to cnt, because we have n digits, the first is 1, the others are 0
        cnt += n

        # Subtract 1, because we don't want to count the number 11, 111, 1111
        cnt -= 1

        # Subtract n - 1, because we don't want to count the numbers with one zero
        # Example: 1001, 10001, ...
        cnt -= n - 1

    # Count the numbers that end with 1
    if n >= 2:
        # Add 1 to cnt, because we have n - 1 digits, the last is 1, the others are 0
        cnt += 1

        # Subtract n - 2, because we don't want to count the number 01, 001, ...
        cnt -= n - 2

    return cnt
