
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for num_str in range(10 ** (n - 1), 10 ** n):
        if num_str > 0 and num_str % 10 == 1:
            result += 1
    return result

