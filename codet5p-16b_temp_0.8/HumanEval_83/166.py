
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(n):
        num_str = str(i + 1)
        if num_str[0] == '1' or num_str[-1] == '1':
            count += 1
    return count

