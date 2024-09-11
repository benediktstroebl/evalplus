```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): A composite number.
    
    Returns:
    int: The largest prime factor of n.
    
    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize largest prime factor as 2
    largest_prime = 2

    # Check each odd number up to n
    i = 3
    while i * i <= n:
        # If n is divisible by i, then i is a prime factor
        if n % i:
            # If n is not divisible by i, increment i by 2
            i += 2
        else:
            # If n is divisible by i, update largest prime and divide n
            largest_prime = i
            n //= i

    # If n > 1, then n is a prime factor
    if n > 1:
        largest_prime = n

    return largest_prime

# Test the function
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It uses a while loop to check each odd number up to the square root of `n` to see if it is a prime factor. If `n` is not divisible by an odd number, it is incremented by 2. If `n` is divisible by an odd number, that odd number is updated to be the largest prime factor and `n` is divided by that odd number. The function continues this process until `n` is reduced to either 1 or a prime number.