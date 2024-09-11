```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.
    
    Args:
        n (int): A positive integer greater than 1.
    
    Returns:
        int: The largest prime factor of n.
    """
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Start checking from 2
    i = 2
    
    # Continue checking until the square root of n
    while i * i <= n:
        # If n is divisible by i, it is a factor
        if n % i:
            # If not, increment by 1
            i += 1
        else:
            # Update the largest factor
            largest_factor = i
            # Divide n by the factor to reduce the size
            n //= i
    
    # In the end, n is the largest prime factor
    return n

# Example usage:
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script uses a trial division method to find the largest prime factor. It starts by checking divisibility of `n` by increasing integers `i` until the square root of `n`, and updates the largest factor whenever a factor is found. At the end of the loop, `n` itself is the largest prime factor, so it is returned as a result.