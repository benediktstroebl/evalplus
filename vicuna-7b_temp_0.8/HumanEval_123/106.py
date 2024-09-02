
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
    n = abs(int(n)) # make sure n is an integer
    if n > 1:
        list1 = get_odd_collatz(3*n+1) # all numbers will be odd
        list2 = get_odd_collatz(3*n+2) # all numbers will be odd
        list3 = get_odd_collatz(3*n+4) # all numbers will be odd
        list4 = get_odd_collatz(3*n+5) # all numbers will be odd
        list5 = get_odd_collatz(3*n+6) # all numbers will be odd
        list6 = get_odd_collatz(3*n+8) # all numbers will be odd
        list7 = get_odd_collatz(3*n+9) # all numbers will be odd
        list8 = get_odd_collatz(3*n+12) # all numbers will be odd
        list9 = get_odd_collatz(3*n+13) # all numbers will be odd
        list10 = get_odd_collatz(3*n+16) # all numbers will be odd
        list11 = get_odd_collatz(3*n+17) # all numbers will be odd
        list12 = get_odd_collatz(3*n+18) # all numbers will be odd
        list13 = get_odd_collatz(3*n+24) # all numbers will be odd
        list14 = get_odd_collatz(3*n+25) # all numbers will be odd
        list15 = get_odd_collatz(3*n+27) # all numbers will be odd
        list16 = get_odd_collatz(3*n+28) # all numbers will be odd
        list17 = get_odd_collatz(3*n+32) # all numbers will be odd
        list18 = get_odd_collatz(3*n+33) # all numbers will be odd
        list19 = get_odd_collatz(3*n+36) # all numbers will be odd
        list20 = get_odd_
