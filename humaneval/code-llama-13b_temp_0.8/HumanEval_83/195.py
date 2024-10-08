
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # Loop from 10 to 10n, counting the numbers that start with 1
    for i in range(10, 10*n+1):
        # Test the last digit of the number
        if str(i)[-1] == '1':
            count += 1
    # Loop from 10 to 10n, counting the numbers that end with 1
    for i in range(10, 10*n+1):
        # Test the first digit of the number
        if str(i)[0] == '1':
            count += 1
    return count

