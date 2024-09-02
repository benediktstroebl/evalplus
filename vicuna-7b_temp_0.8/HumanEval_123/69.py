
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
    # Check if n is 1 or 2
    if n == 1 or n == 2:
        return [n]
    else:
        # Get the last odd number in collatz sequence
        last_odd = get_odd_collatz(n // 2)[-1]
        # Add 1 to last odd number if the n is even
        if n % 2 == 0:
            last_odd += 1
        # Add all the odd numbers in collatz sequence up to n
        return [last_odd] + get_odd_collatz(n // 2)
