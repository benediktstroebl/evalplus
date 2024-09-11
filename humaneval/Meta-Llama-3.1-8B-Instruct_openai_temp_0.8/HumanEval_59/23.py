```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """

    # Start checking from the largest prime factor, which is n // 2
    i = n // 2
    while i > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                return i
        i -= 1

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

However, if you need a more efficient solution, you can optimize it by only checking up to the square root of `n` for prime factors. Also, instead of checking manually whether a number is prime, we can use the `math.isqrt` function to efficiently calculate the square root of `n`.

```python
import math

def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """

    # Start checking from the largest prime factor, which is n // 2
    i = n // 2
    while i > 1:
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if all(i % j!= 0 for j in range(2, math.isqrt(i) + 1)):
                return i
        i -= 1

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

Or, we can even optimize it further by using a more efficient algorithm to find prime factors, such as the Sieve of Eratosthenes. 

```python
import math

def sieve_of_eratosthenes(n: int) -> list:
    """
    Return a list of all prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime
    for current_prime in range(2, int(math.sqrt(n)) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime * current_prime, n + 1, current_prime):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.
    """

    # Get all prime numbers up to n
    primes = sieve_of_eratosthenes(n)
    
    # Check if n is prime and return it, otherwise find largest prime factor
    if n