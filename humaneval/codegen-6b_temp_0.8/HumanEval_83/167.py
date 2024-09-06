
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Base case
    if n == 1:
        return 1

    # Pass
    if n == 2:
        return 4

    # If n is 2, since there are 4 numbers that start or end with 1, return the value of 4.
    if n == 3:
        return 9

    # Otherwise, include i-digits that start or end with 1, where 1 is 1, 2, or 3 digits long,
    # and i is the number of digits in the integer
    count = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += starts_one_ends(i) * starts_one_ends(n - i)
    return count

