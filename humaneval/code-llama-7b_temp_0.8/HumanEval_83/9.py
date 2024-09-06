
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Variables used for storing result.
    count = 0

    # We first check if n is less than or equal to 1.
    # We then start with 10 and keep dividing n until we get 1 as quotient.
    # We keep incrementing the count of n-digit numbers that start with 1.
    # We then check the count of n-digit numbers that end with 1.
    # Finally, return the count of numbers that start or end with 1.
    while n > 1:
        if n % 10 == 1:
            count += 1
        n //= 10
    return count * 10 + (10 if n == 1 else 0)

