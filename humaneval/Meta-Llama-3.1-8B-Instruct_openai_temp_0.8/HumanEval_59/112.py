### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines a function `largest_prime_factor(n: int)` that calculates the largest prime factor of a given number `n`. The function uses a simple loop to check divisors up to the square root of `n` and returns the remaining number, which is the largest prime factor.

The time complexity of this algorithm is O(sqrt(n)) because the loop runs up to the square root of `n`. This makes it efficient for large inputs.