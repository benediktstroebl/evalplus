
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

    # If input is 1, return 1.
    if n == 1:
        return [1]

    # Initialize odd_collatz as list of 1, which is the smallest odd collatz number.
    odd_collatz = [1]

    # Initialize n as input.
    n = int(n)

    # Repeat the loop until n is 1.
    while n!= 1:

        # If n is even, n = n/2.
        if n % 2 == 0:
            n /= 2
        # If n is odd, n = (3n + 1).
        else:
            n = (3 * n) + 1

        # Append n to odd_collatz.
        odd_collatz.append(n)

    # Return sorted odd_collatz.
    return sorted(odd_collatz)
