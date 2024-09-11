```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        List[int]: A list of prime factors.
    """
    
    def sieve_of_eratosthenes(n: int) -> List[bool]:
        """ 
        Helper function to generate prime numbers less than n.
        
        Args:
            n (int): The maximum number to check for primality.
        
        Returns:
            List[bool]: A boolean array indicating whether each number is prime.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    primes = [p for p in range(2, n + 1) if sieve_of_eratosthenes(n)[p]]
    factors = []
    
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    
    if n > 1:
        factors.append(n)
    
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses the Sieve of Eratosthenes algorithm to generate prime numbers up to the input number `n`. It then iterates over these primes to find the prime factors of `n`.