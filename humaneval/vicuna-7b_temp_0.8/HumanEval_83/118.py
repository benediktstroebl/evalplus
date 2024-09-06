
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Using a list comprehension to count the number of n-digit numbers
    # that start with 1 or end with 1
    num = 0
    for i in range(n):
        if n % i == 0 and n // i == 1 or n % i == 1:
            num += 1
    return num
