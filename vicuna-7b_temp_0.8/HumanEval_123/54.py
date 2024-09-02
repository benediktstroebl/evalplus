
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
    collatz_list = []
    # 初始化collatz列表
    collatz_list.append(n)
    # 遍历所有的偶数
    while collatz_list:
        # 从列表沿从后遍历
        for i in range(len(collatz_list) - 1):
            # 如果前面的数是偶数，则将后面的数设为它的半数
            if collatz_list[i] % 2 == 0:
                collatz_list[i:i + 2] = [collatz_list[i], collatz_list[i + 1] / 2]
            else:
                collatz_list[i:i + 3] = [collatz_list[i], collatz_list[i + 1] * 3 + 1]
    return collatz_list
