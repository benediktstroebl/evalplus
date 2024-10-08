

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
    import math
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    if len(lst) == 1:
        return int(str(lst[0]))
    elif len(lst) == 2:
        return int(str(max(lst))[0])
    max_num = max(lst)
    if max_num % 2 == 0:
        return 0
    for i in range(len(primes)):
        if primes[i] > math.sqrt(max_num):
            break
        if max_num % primes[i] == 0:
            return 0
    sum_lst = []
    for i in lst:
        new_num = int(str(i))
        sum_lst.append(new_num)
    return sum(sum_lst)
