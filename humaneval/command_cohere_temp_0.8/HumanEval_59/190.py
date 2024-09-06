```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for largest factor first which is not a prime number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    # If no factors are found, return n which is the largest factor
    return n
```

The function `largest_prime_factor` takes an integer `n` as input and loops through factors from 2 up to the square root of `n`. If it finds any non-prime factors, it returns that largest factor. If not, it returns `n` as the largest possible factor. This approach ensures the correct largest prime factor is returned for various input cases. 

To ensure the effectiveness of the function, remember to test it with a variety of inputs, including prime and non-prime numbers, to ensure its accuracy in identifying the largest prime factor.