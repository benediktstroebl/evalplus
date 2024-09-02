
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # adding 10 to n, since we want to include digits 0-9.
    for i in range(1, n + 10):
        str_i = str(i)
        if str_i[0] == '1' or str_i[-1] == '1':
            count += 1

    return count
