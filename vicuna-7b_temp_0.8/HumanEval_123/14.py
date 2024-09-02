
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
    # Convert the integer to a string
    str_n = str(n)
    # Remove the '0' from the right end of the string
    str_n = str_n[:-3]
    # Split the string into a list of digits
    n = [int(digit) for digit in str_n]
    # Check if the number is odd or not
    if n[-1] % 2 == 1:
        # Get the left part of the collatz sequence
        left = get_odd_collatz(n[:-1])
        # Get the right part of the collatz sequence
        right = get_collatz(n[-1])
        # Combine the left and right part of the collatz sequence
        return left + [right]
    else:
        return []
