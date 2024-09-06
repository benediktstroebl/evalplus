
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    def is_prime(x):
        if x <= 1:
            return False
        for p in range(2, x):
            if x % p == 0:
                return False
        return True
    
    def __iterate(x):
        for i in range(1, int(x ** 0.5) + 1):
            if is_prime(x * i):
                yield x * i
                for j in range(i + 1, int(x ** 0.5) + 1):
                    if is_prime(x * j):
                        yield x * j
    n = max(n, 2)
    primes = list(__iterate(n))
    return primes[:n-1]
