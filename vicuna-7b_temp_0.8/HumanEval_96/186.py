
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
    def sieve(m):
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def count_up_to_n(n):
        primes = []
        for i in range(1, int(n ** 0.5) + 1):
            if sieve(i):
                for j in range(i, n + 1):
                    if not is_prime(j):
                        break
                    primes.append(j)
        return primes
    
    return count_up_to_n(n)
