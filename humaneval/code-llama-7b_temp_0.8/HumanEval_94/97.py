

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
    from math import sqrt
    from random import randint
    import primefac

    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0 and n != 2:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def find_factors(n):
        return list(primefac.primefac(n))

    def prime_digit_sum(n):
        if is_prime(n):
            return sum([int(i) for i in str(n)])
        else:
            return 0

    def digit_sum(n):
        return sum([int(i) for i in str(n)])

    def find_largest_prime(lst):
        p = max([lst[i] for i in range(len(lst))], key=prime_digit_sum)
        return p

    p = find_largest_prime(lst)
    #p = max(lst, key=prime_digit_sum)
    return digit_sum(p)




































































































































































































































