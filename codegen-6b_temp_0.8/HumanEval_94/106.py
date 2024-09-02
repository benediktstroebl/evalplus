

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
    numbers = [int(x) for x in lst]

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primes2 = [2, 2, 2, 3, 5, 5, 7, 7, 11, 11, 13, 13, 17, 17, 19, 19, 23, 23, 29, 29, 31, 31, 37, 37, 41, 41, 43, 43, 47, 47, 53,
               53, 59, 59, 61, 61, 67, 67, 71, 71, 73, 73, 79, 79, 83, 83, 89, 89, 97, 97, 101, 101, 103, 103, 107, 107, 109,
               109, 113, 113, 127, 127, 131, 131, 137, 137, 139, 139, 149, 149, 151, 151, 157, 157, 163, 163, 167,
               167, 173, 173, 179, 179, 181, 181, 191, 191, 193, 193, 197, 197, 199, 199, 211, 211, 223, 223, 227,
               227, 229, 229, 233, 233, 239, 239, 241, 241, 251, 251, 257, 257, 263, 263]

    result = 0
    for n in numbers:
        for p in primes:
            if n % p == 0:
                if n in primes2:
                    result += primes.index(p)
                for i in range(1, len(str(n))):
                    num = n % 10
                    if num in primes:
                        result += primes.index(num)
                    n //= 10
                return result

