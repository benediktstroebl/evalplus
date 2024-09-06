
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n <= 0:
        return []
    elif n % 2 == 0:
        # get the half of n
        n_half = n // 2
        # get the collatz sequence of n_half
        collatz_n_half = get_odd_collatz(n_half)
        return collatz_n_half
    else:
        # get the 3 times n + 1
        n_3times_plus_1 = n * 3 + 1
        # get the collatz sequence of n_3times_plus_1
        collatz_n_3times_plus_1 = get_odd_collatz(n_3times_plus_1)
        # return the odd numbers in collatz sequence of n_3times_plus_1
        return [x for x in collatz_n_3times_plus_1 if x % 2 != 0]
