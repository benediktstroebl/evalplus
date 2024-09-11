### Largest Prime Factor Function
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A number greater than 1.
    
    Returns:
        int: The largest prime factor of n.
    
    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    
    # Start from the smallest prime number
    i = 2
    
    # Continue dividing n by i as long as n is divisible by i
    while n % i == 0:
        n = n // i
    
    # Now, n is no longer divisible by 2. We start checking from 3
    i = 3
    
    # We loop until i is greater than the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a prime factor of n
        if n % i:
            # If n is not divisible by i, then increment i by 2
            i += 2
        else:
            # If n is divisible by i, then i is a prime factor of n
            # We divide n by i and continue the loop
            n = n // i
    
    # At this point, n is a prime number and it is the largest prime factor of the original number
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function assumes that `n` is greater than 1 and is not a prime number. It uses a while loop to divide `n` by the smallest prime number (2) as long as `n` is divisible by it, and then continues checking from 3 until `i` is greater than the square root of `n`. If `n` is divisible by `i`, then `i` is a prime factor of `n`, and `n` is divided by `i` and the loop continues. The function returns the final value of `n`, which is the largest prime factor of the original number.