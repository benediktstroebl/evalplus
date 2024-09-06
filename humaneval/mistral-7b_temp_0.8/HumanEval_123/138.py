
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
    # TODO: Write your code here.
    return [1, 15, 25, 75, 225, 675, 2025, 6075, 18225, 54675, 164025, 492075, 1476225, 4428675, 13285925, 39857775, 119573325, 358719975, 1076159925, 322847975, 968543925, 280562175, 841686525, 2525059575, 757517875, 2272553625, 6817660625, 20452982125, 
