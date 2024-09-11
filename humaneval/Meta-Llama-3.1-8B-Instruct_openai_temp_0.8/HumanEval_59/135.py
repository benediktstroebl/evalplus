```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: A positive integer greater than 1.
    :return: The largest prime factor of n.
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

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a while loop to divide `n` by the smallest prime factor it finds until `n` is no longer divisible. At this point, `n` is the largest prime factor of the original number. The test cases at the end verify that the function works correctly for two examples.