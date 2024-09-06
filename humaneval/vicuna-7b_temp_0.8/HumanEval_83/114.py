
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Check if n is 1 or 2
    if n == 1 or n == 2:
        return 1
    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Check if the number starts with 1
        if i == 1:
            # Check if the number ends with 1
            if i == str(i)[-1]:
                return 1
        # Check if the number ends with 1
        if i % 10 == 1:
            return 1
    # Should never get here
    return 0