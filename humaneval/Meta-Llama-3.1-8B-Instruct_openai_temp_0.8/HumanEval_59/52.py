### Largest Prime Factor of a Number
#### Problem Description

Given a number `n` (where `n > 1` and `n` is not a prime), find the largest prime factor of `n`.

#### Solution

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Args:
    n (int): A number greater than 1 and not a prime.
    
    Returns:
    int: The largest prime factor of n.
    
    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    # Initialize the largest prime factor to 1
    largest_factor = 1
    
    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Assume i is prime
            is_prime = True
            
            # Check if i is prime by dividing it by all numbers less than i
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    # If i is divisible by j, it's not prime
                    is_prime = False
                    break
            
            # If i is prime and it's a factor of n, update the largest factor
            if is_prime and n % i == 0:
                largest_factor = i
    
    # Return the largest prime factor
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

However, this solution has an upper limit of n * sqrt(n) because it checks all numbers up to the square root of n for divisibility. This can be optimized by using a more efficient algorithm.

### Optimized Solution

To optimize the solution, we can use a more efficient algorithm to find the largest prime factor, which is the Sieve of Eratosthenes algorithm combined with a loop to find the largest prime factor.

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Args:
    n (int): A number greater than 1 and not a prime.
    
    Returns:
    int: The largest prime factor of n.
    
    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    
    # Initialize the largest prime factor to 1
    largest_factor = 1
    
    # Find the prime factors up to n using the Sieve of Eratosthenes algorithm
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    # Find the largest prime factor
    for i in range(n, 1, -1):
        if sieve[i] and n % i == 0:
            largest_factor = i
            break
    
    # Return the largest prime factor
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This optimized solution has a time complexity of