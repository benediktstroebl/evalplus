
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
    # return an empty list if n is negative
    if n < 1:
        return []
    #  create an empty list to store the odd numbers
    odd_numbers = []
    # initialize the current number to n
    current_num = n
    # start the loop at 1
    num = 1
    # keep track of the number of elements in the list
    list_size = 0
    # loop while the current number is not 1
    while current_num != 1:
        # if the current number is odd, add it to the list
        if current_num % 2 == 1:
            odd_numbers.append(current_num)
            list_size += 1
        # if the current number is even, multiply it by 3 and add 1
        current_num = 3 * current_num + 1
        num += 1
    # return the odd numbers in the list sorted in increasing order
    return sorted(odd_numbers[:list_size])
