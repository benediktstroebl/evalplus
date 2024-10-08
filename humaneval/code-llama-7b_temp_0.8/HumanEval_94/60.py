

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

    def isprime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        k = int(math.sqrt(n)) + 1
        for p in range(5, k + 1, 6):
            if n % p == 0 or n % (p + 2) == 0:
                return False
        return True

    print(lst)

    lst_filtered = list(filter(lambda x: x > 0, lst))
    print(lst_filtered)

    lst_primes = []
    for i in lst_filtered:
        if isprime(i):
            lst_primes.append(i)

    print(lst_primes)

    lst_primes_sum = 0
    for i in lst_primes:
        i_str = str(i)
        i_sum = 0
        for c in i_str:
            i_sum += int(c)
        lst_primes_sum += i_sum

    return lst_primes_sum

