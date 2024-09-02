
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
    even_nums = []
    odd_nums = []
    curr_num = n
    while curr_num != 1:
        if curr_num % 2 == 0:
            even_nums.append(curr_num)
        else:
            odd_nums.append(curr_num)
        curr_num = curr_num*3 + 1
    sorted_odd_nums = sorted(odd_nums)
    return sorted_odd_nums + even_nums


"""
Binary search

Given a sorted list of integers, search a target value, and return the position of the target.
If the target is not found, return -1.

Note:
    If the list is empty, return -1.
    You may assume that all elements in the list are unique.
    Your algorithm's runtime complexity must be in the order of O(log n).
    Example:
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: 2
"""