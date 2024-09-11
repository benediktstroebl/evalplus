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
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It starts by dividing `n` by the smallest prime number, 2, and continues dividing by increasing integers until it finds a divisor. If `n` is not divisible by the current value of `i`, it increments `i` by 1. Once `n` is reduced to a prime number, that prime number is the largest prime factor of the original `n`.