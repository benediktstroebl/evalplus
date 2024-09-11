```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of n.

    Examples:
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

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script works by iteratively dividing the input number `n` by the smallest prime number (2) as long as it's divisible. If `n` is not divisible by 2, it increments the divisor `i` by 1. This process continues until `i` squared is greater than `n`. At this point, `n` is either a prime number itself or the largest prime factor of the original number. The function returns `n`, which is the largest prime factor. 

However, this function has some limitations. For example, for very large inputs (e.g., numbers with millions of digits), the function may take a long time to run because it uses a trial division method. A more efficient approach would be to use the Sieve of Eratosthenes to generate prime numbers up to the square root of `n` and then check if `n` is divisible by any of these primes.