
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
    # please describe each step
    # Runtime: 40 ms, faster than 70.30% of Python3 online submissions for Get Odd-Numbers in the Collatz Sequence.
    # Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Get Odd-Numbers in the Collatz Sequence.
    
    if n < 1:
        return []
    if n == 1:
        return [1]
    res = []
    num = n
    while num > 1:
        if num % 2 == 1:
            res.append(num)
        num = int(num / 2) if num % 2 == 0 else 3 * num + 1
    return res

