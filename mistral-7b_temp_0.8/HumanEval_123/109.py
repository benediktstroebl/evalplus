
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
    # if n==1:
    #     return [1]

    # 1. init a list, max_num is 1000000
    # 2. start with n, find next odd number
    # 3. put it into the list if it's not in the list
    # 4. find next odd number
    # 5. while the odd number is not 1 and it's not in the list
    # 6. the list is the result

    max_num = 1000000
    numbers = [1]
    while n < max_num:
        if n % 2 == 1:
            # even
            if n not in numbers:
                numbers.append(n)
            n = 3*n + 1
        else:
            # odd
            if n not in numbers:
                numbers.append(n)
            n = n//2

    return numbers

