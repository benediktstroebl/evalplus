
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
    ## EDGE CASES ##
    if not n:
        return []

    # don't know the result, let's try to find it
    # CODE GOES HERE
    # with this method, the results is sorted
    # but in fact, the requirement was to return
    # the sequence in order of appearance
    # in order to find the O(1) solution, I need to use a list
    # to keep track of the odd elements
    result = []
    result_l = []
    while n != 1:
        result.append(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1

    for num in result:
        if num % 2 == 1:
            result_l.append(num)

    return result_l

    #return [num for num in result if num % 2 == 1]
