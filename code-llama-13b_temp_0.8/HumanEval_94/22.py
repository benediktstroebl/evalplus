

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

    # 1
    # primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
    # is_prime = lambda x : x in primes

    # 2
    # is_prime = lambda x: 1 not in [x % i for i in range(2,int(x**0.5)+1)]

    # 3
    is_prime = lambda x: 1 not in [x % i for i in range(2,int(x/2)+1)]

    def digits(n):
        if n == 0:
            return []
        else:
            return [int(n%10)] + digits(int(n/10))

    # print(is_prime(151))
    # print(is_prime(150))
    # print(digits(151))
    # print(digits(150))
    # print(is_prime(29))
    # print(is_prime(181))
    # print(digits(181))

    return sum(digits(max(filter(is_prime, lst))))






