
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
    ## HINT: You may need to import the "collections" module.
    ## Also, check that you are using the right collatz function.

    ## write your code here
    from collections import deque

    collatz = deque([n])
    odd_collatz = []
    while collatz:
        if collatz[0] % 2 == 1:
            odd_collatz.append(collatz[0])
        collatz.append(3 * collatz[0] + 1 if collatz[0] % 2 == 0 else collatz[0] / 2)
        collatz.popleft()
    return sorted(odd_collatz)
