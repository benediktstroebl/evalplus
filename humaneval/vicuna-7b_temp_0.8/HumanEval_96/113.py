
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
        """
        helper function to check if n is prime
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_primes(n):
        """
        helper function to get the prime numbers less than n
        """
        primes = []
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i):
                primes.append(i)
        return primes
    
    def get_count(n):
        """
        helper function to get the count of prime numbers less than n
        """
        count = 0
        primes = get_primes(n)
        for prime in primes:
            if prime <= n:
                count += 1
        return count
    
    n = int(input("Enter an integer: "))
    primes = get_primes(n)
    count = get_count(n)
    return primes[count:]
