### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    This function works by dividing the input number n by the smallest prime number (2) as long as it's divisible.
    Then it increments the divisor by 1 and continues the process with the new divisor until n is reduced to 1.
    The last divisor used will be the largest prime factor of n.

    Args:
        n (int): A composite number greater than 1.

    Returns:
        int: The largest prime factor of n.

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

This Python script defines a function `largest_prime_factor` that finds the largest prime factor of a given composite number `n`. It uses a while loop to divide `n` by the smallest prime number (2) as long as it's divisible. The loop continues with the next prime number until `n` is reduced to 1, at which point the last divisor used is the largest prime factor of `n`. The function returns this largest prime factor.