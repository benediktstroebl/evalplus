
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
    cache = {}
    cache[1] = [1]
    cache[2] = [2]
    cache[3] = [3]
    cache[4] = [4]
    
    def collatz_next(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1
    
    def collatz(n):
        if n in cache:
            return cache[n]
        
        collatz_list = [n]
        while n != 1:
            n = collatz_next(n)
            collatz_list.append(n)
        cache[n] = collatz_list
        return collatz_list
        
    odd_list = [i for i in collatz(n) if i % 2 != 0]
    return odd_list


