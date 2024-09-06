

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    from math import log, ceil

    # lst_copy = lst[:]
    lst.sort()
    # print(lst)

    # lst = [x for x in lst_copy if x!=0]
    # print(lst)

    def is_prime(n):
        # if n == 1:
        #     return False
        # elif n == 2:
        #     return True
        # else:
        #     x = 2
        #     while x < n:
        #         if n % x == 0:
        #             return False
        #         x += 1
        #     else:
        #         return True

        if n % 2 == 0:
            return False

        for i in range(3, ceil(n ** (1 / 2)), 2):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(num):
        if num == 0:
            return 0

        return (num % 10) + sum_of_digits(num // 10)

    ans = 0
    for n in lst:
        if is_prime(n):
            ans += sum_of_digits(n)

    return ans

import pytest
