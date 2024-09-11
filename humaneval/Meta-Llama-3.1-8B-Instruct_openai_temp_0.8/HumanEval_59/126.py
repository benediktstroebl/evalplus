```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: An integer greater than 1.
    :return: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that calculates the largest prime factor of a given integer `n`. It uses a simple trial division method, iterating from 2 to the square root of `n` and dividing `n` by the current number if it's divisible. If `n` is not divisible, the current number is incremented. Finally, the function returns `n`, which is the largest prime factor of the original `n`.