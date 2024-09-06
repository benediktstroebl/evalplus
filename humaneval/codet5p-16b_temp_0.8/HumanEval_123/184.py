
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

    assert (n >= 1)
    collatz_sequence = []
    # 1. Initialize Collatz Sequence
    collatz_sequence.append(n)

    # 2. While sequence length is smaller than max length
    while len(collatz_sequence) < 1000:
        
        # 3. Check if the previous term is even
        if n % 2 == 0:
            # 4. If it is even, then take the previous term and half it
            n = n // 2
        else:
            # 5. If it is odd, then multiply by 3 and add 1.
            n = 3*n + 1
        
        # 6. Add the term to the Collatz sequence
        collatz_sequence.append(n)

    # 7. Return the odd numbers in the sequence
    return list(set([i for i in collatz_sequence if i % 2 == 1]))
    
