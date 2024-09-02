
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    digit = 1
    for i in range(n + 1):
        if str(i).startswith(str(digit)) or str(i).endswith(str(digit)):
            count += 1
        digit = int(str(digit) + 1)
    return count
