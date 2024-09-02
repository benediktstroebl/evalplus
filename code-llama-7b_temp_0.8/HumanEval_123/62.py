
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
    # initialize the list of odd collatz values
    odd_collatz_list = []

    # initialize the starting number
    n = 1

    # check the conditions to add the number to the list
    while n != 1:
        if n % 2 != 0:
            odd_collatz_list.append(n)
            n = 3 * n + 1

        else:
            n = n // 2

    # return the list of odd collatz values
    return odd_collatz_list
