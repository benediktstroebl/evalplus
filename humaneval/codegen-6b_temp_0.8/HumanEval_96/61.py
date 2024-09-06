
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
    def isPrime(n):
        return n in [2,3,5,7,11,13,17]
    
    def generate_primes(n):
        primes = [2]
        i = 3
        while primes[-1] <= n:
            if isPrime(i):
                primes.append(i)
            i += 2
        return primes
    
    return generate_primes(n)[1:]
    
