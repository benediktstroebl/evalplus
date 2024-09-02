
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    count = 0
    n_str = str(n)
    if n_str[0] == '1':
        count += 1
    if n_str[-1] == '1':
        count += 1
    return count

