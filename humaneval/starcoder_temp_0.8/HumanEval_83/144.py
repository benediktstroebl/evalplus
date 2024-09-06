
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Decompose n into a sum of powers of 10:
    # n = sum(10^k * a_k)
    # where a_k is in {0, 1}
    # This allows us to solve the problem as follows:
    #
    # sum(10^k * a_k) = 10^k * a_k + 10^(k-1) * a_{k-1}
    # if a_k = 1, then we're adding 10^(k-1) to our count.
    # if a_k = 0, then we're skipping 10^(k-1)
    #
    # Since a_0 = 1, we can ignore the last term.

    if n == 1:
        return 1

    n_str = str(n)
    digit_count = len(n_str)
    if n_str[0] == '1' or n_str[-1] == '1':
        return 10 ** (digit_count - 1)
    else:
        return 0
