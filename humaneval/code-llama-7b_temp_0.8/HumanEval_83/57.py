
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_ones = n-1
    two_n_ones = n - 2
    n_zeros = n - (n_ones + two_n_ones)
    n_threes = n - (n_ones + n_zeros)
    n_fours = n - (n_ones + n_zeros + n_threes)
    n_fives = n - (n_ones + n_zeros + n_threes + n_fours)
    n_sixes = n - (n_ones + n_zeros + n_threes + n_fours + n_fives)
    return n_ones * 10**n_ones + n_zeros * 10**n_zeros + n_threes * 10**n_threes + n_fours * 10**n_fours + n_fives * 10**n_fives + n_sixes * 10**n_sixes

