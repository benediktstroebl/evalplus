
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # keep track of the total count
    total = 0
    # convert n to a string
    n_str = str(n)
    # find the length of the string
    n_len = len(n_str)
    # loop from 1 to n_len (inclusive)
    for i in range(1, n_len+1):
        # compute the number of combinations for the starting digits
        start = n_len - i
        # compute the number of combinations for the ending digits
        end = i - 1
        # compute the total number of combinations
        total += 10**start * 10**end
    # compute the number of combinations for the middle digits
    middle = n_len - 2
    # compute the number of combinations for the middle digits
    total += 10**middle
    # return the total number of combinations
    return total

