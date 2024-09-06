

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        prime_factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                n //= i
                prime_factors.append(i)
            else:
                i += 1
        if n > 1:
            prime_factors.append(n)
        return prime_factors

    prime_factors = get_prime_factors(n)
    largest_factor = max(prime_factors)
    return largest_factor

