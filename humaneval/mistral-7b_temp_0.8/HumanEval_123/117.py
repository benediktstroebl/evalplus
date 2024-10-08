
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
    # Your code here

    ######## test code ########
    from unittest import main

    def test_get_odd_collatz():
        assert get_odd_collatz(1) == [1]
        assert get_odd_collatz(2) == [1]
        assert get_odd_collatz(3) == [1, 3]
        assert get_odd_collatz(4) == [1]
        assert get_odd_collatz(5) == [1, 5]
        assert get_odd_collatz(6) == [1, 5, 17]
        assert get_odd_collatz(7) == [1, 7]
        assert get_odd_collatz(8) == [1]
        assert get_odd_collatz(9) == [1, 3, 9]
        assert get_odd_collatz(10) == [1, 5, 17, 13]
        assert get_odd_collatz(11) == [1, 3, 11]
       
