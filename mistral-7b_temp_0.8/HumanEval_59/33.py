

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    """
    This function uses the sieve of Eratosthenes to generate a list of prime numbers up to the square root of the input number.
    Then, it uses the binary search algorithm to search for the largest prime factor of the input number in the list of prime numbers.
    """

    primes = [2]
    for i in range(3, n // 2 + 1, 2):
        if i not in primes:
            primes.append(i)
            for j in range(i * i, n, i * 2):
                primes.remove(j)

    low = 1
    high = len(primes)
    while low < high:
        mid = (low + high) // 2
        if primes[mid] > n // primes[mid]:
            high = mid
        else:
            low = mid + 1
    return primes[low - 1]

