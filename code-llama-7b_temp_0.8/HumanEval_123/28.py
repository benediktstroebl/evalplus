
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
    # init variables
    sequence = [n]
    flag = True
    while flag:
        # if even, then: number/2
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1]//2)
        # if odd, then: 3*number+1
        else:
            sequence.append(3*sequence[-1]+1)
        # if the latest number is 1, then finish the loop
        if sequence[-1] == 1:
            flag = False
    # remove the number that is not in odd collatz
    sequence = [x for x in sequence if x % 2 != 0]
    return sequence

