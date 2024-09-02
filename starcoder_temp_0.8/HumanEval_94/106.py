

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
    lst2 = []
    for x in lst:
        lst2.append(x)
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num > 2 and num % 2 == 0:
            return False
        for x in range(3, int(num**0.5)+2, 2):
            if num % x == 0:
                return False
        return True

    def get_prime(n):
        for x in range(n):
            if is_prime(x) == True:
                yield x

    primes = get_prime(max(lst2)+1)
    for x in lst2:
        prime = primes.next()
        while prime < x:
            prime = primes.next()
        lst2[lst2.index(x)] = prime
    lst2 = lst2 + [0]
    result = sum(lst2)
    return result
