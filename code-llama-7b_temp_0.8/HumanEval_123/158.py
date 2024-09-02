
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
    #check the input
    if n <= 0:
        raise ValueError('Please input positive integer')

    # init
    odd_collatz = []
    check = set()

    # loop until collatz reach 1
    while n != 1:
        if n in check:
            break
        check.add(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    # if n is in check, then the collatz sequence is 1
    if n in check:
        return [1]
    
    # loop from n to 1
    while n > 1:
        if n % 2 == 0:
            odd_collatz.append(n // 2)
            n = n // 2
        else:
            odd_collatz.append(3 * n + 1)
            n = 3 * n + 1
    
    return odd_collatz


