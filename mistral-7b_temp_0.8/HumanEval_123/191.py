
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

    """
    Input: 
        n: an integer >= 1

    Output:
        a list containing the odd numbers in the collatz sequence for n
    """

    # initialize an empty list to store odd numbers in collatz sequence
    odd_collatz_list = []

    # base case
    if n == 1:
        return odd_collatz_list

    # start from 2 to n and check if it is odd number
    for num in range(2, n+1):
        # append current number to the list if it is odd number
        if num % 2 != 0:
            odd_collatz_list.append(num)

    # return the list
    return odd_collatz_list

