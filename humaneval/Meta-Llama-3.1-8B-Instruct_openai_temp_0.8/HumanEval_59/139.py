```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: Input number
    :return: The largest prime factor of n
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

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It does this by continuously dividing `n` by the smallest divisor (starting from 2) until it can no longer be divided. The remaining number is the largest prime factor. The script then includes two test cases to verify that the function works as expected.