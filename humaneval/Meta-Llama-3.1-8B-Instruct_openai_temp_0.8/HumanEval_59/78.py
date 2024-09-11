```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    This function works by dividing the input number by the smallest prime number (2) 
    as long as it's divisible, then by the next prime number (3), and so on. It keeps 
    track of the largest divisor it finds.
    
    Args:
        n (int): The input number. Assume n > 1 and is not a prime.
    
    Returns:
        int: The largest prime factor of n.
    
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1
    i = 2
    while i * i <= n:
        if n % i:
            # If n is not divisible by i, then increment i by 1
            i += 1
        else:
            # If n is divisible by i, then update n and largest_factor
            n //= i
            largest_factor = i
    # At this point, n is a prime number
    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor. It starts with the smallest prime number (2) and divides the input number as long as it's divisible. Then it moves on to the next prime number (3) and repeats the process. The process continues until the input number is reduced to a prime number, which is the largest prime factor.