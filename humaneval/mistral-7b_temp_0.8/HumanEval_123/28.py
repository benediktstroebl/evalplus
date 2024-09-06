
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
    # YOUR CODE HERE
    # list = []
    # for i in range(1, n+1):
    #     if i % 2 == 1:
    #         # print(f"{i}")
    #         if i == 1:
    #             list.append(i)
    #         elif i % 2 == 1:
    #             if len(list) == 0:
    #                 list.append(i)
    #             else:
    #                 list.append(i)
    #                 list.sort()
    # print(list)
    # return list
    return [i for i in range(1,n+1) if i % 2 == 1 and (len(list) == 0 or (len(list) != 0 and i > list[-1]) )]
