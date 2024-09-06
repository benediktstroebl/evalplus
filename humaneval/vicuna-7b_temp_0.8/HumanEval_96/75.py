
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
    def is_prime(n):
        """Return True if n is prime, False otherwise."""
        if n < 2:
            return False
        for _ in range(2, int(n**0.5) + 1):
            if n % _ == 0:
                return False
        return True

    def get_primes(n):
        """Return a list of prime numbers less than n."""
        primes = []
        for p in range(2, int(n**0.5) + 1):
            if is_prime(p):
                primes.append(p)
        return primes

    n = int(n)
    primes = get_primes(n)
    result = []
    while len(result) < n:
        p = primes[0]
        for p1 in primes:
            if p*p1 > n:
                break
        result.append(p)
    return result
