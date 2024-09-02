

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    # algorithm 1: recursion
    # def sum_to_n_recursion(n: int):
    #     if n == 1:
    #         return 1
    #     return n + sum_to_n_recursion(n-1)

    # return sum_to_n_recursion(n)

    # algorithm 2: iteration
    num = 1
    result = 0
    while num <= n:
        result += num
        num += 1
    return result

