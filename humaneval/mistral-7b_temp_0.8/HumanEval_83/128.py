
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    n = n -1
    count = 0

    # if the last digit is one
    if n % 10 == 1:
        count += 1

    # if the first digit is one
    if n // 10 == 1:
        count += 1

    # if the last two digits are 11
    if n % 100 == 11:
        count += 1

    # if the first two digits are 11
    if n // 100 == 11:
        count += 1

    # if the last three digits are 111
    if n % 1000 == 111:
        count += 1

    # if the first three digits are 111
    if n // 1000 == 111:
        count += 1

    return count
