
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    num_start_end = 0
    for i in range(1, n+1):
        num_str = str(i)
        if num_str[0] == '1' or num_str[-1] == '1':
            num_start_end += 1
    return num_start_end
