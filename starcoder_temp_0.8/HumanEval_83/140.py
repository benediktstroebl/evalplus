
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    ones_count = 0
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] == "1" or n_str[i] == "0" and i == 0:
            ones_count += 1
        elif n_str[i] == "1" or n_str[i] == "0" and i == len(n_str) - 1:
            ones_count += 1
    return ones_count
