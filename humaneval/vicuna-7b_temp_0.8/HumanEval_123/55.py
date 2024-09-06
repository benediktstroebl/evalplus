
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
    # Collatz(n) returns the Collatz sequence for n
    # We are interested in the odd numbers in the sequence
    # Sort the list in increasing order
    collatz_list = sorted(range(1, n + 1), key=lambda x: x // 2 if x % 2 == 0 else x)
    # Get the indices of the odd numbers
    odd_indices = [i for i, x in enumerate(collatz_list) if x % 2 == 1]
    # Get the odd numbers
    odd_numbers = collatz_list[odd_indices]
    return odd_numbers
