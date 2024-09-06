

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Your code here
    # from math import sqrt
    #
    # largest = 1
    # # if n < 2:
    # #     return 1
    # if n % 2 == 0:
    #     largest = 2
    #
    # for i in range(3, int(sqrt(n)), 2):
    #     if n % i == 0:
    #         largest = i
    #
    # if n % 3 == 0:
    #     largest = 3
    #
    # return largest
    # O(sqrt(n))
    # O(sqrt(n))
    # if n <= 1:
    #     return 1
    # if n % 2 == 0:
    #     return 2
    # for i in range(3, n, 2):
    #     if n % i == 0:
    #         return i
    # return n
    # O(sqrt(n))
    # O(sqrt(n))
    # if n <= 1:
    #     return 1
    # if n % 2 == 0:
    #     return 2
    # for i in range(3, n, 2):
    #     if n % i == 0:
    #         return i
    # return n
    # O(sqrt(n))
    # O(sqrt(n))
    # if n <= 1:
    #     return 1
    # for i in range(3, n):
    #     if n % i == 0:
    #         return i
    # return n
    # O(sqrt(n))
    # O(sqrt(n))
    if n <= 1:
        return 1
    for i in range(3, n):
        if n % i == 0:
            return i
    return n
    # O(sqrt(n))
    # O(sqrt(n))

