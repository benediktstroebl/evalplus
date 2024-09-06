

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    #This one is really good because it doesn't have a recursion, instead it goes from 2 to sqrt(n)
    #where it divides n, and checks if the result is still whole or not
    #this algorithm is in O(sqrt(n))
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                n /= i
            return i
    return n
