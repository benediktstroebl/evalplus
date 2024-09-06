
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # TIP: The floor of a quotient is the largest integer that does not exceed the given number.
    count = 0
    floor = 10 ** (n - 1)

    for num in range(1, floor):
        #Check if the number starts with 1
        if num // 10 ** (n - 1) == 1:
            count += 1
        # Check if the number ends with 1
        if num % 10 == 1:
            count += 1
    return count
