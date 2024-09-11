### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.

    Parameters:
    n (int): A number greater than 1.

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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This function works by dividing the input number `n` by the smallest prime number, which is 2. If `n` is divisible by 2, we divide it by 2 and repeat the process. If `n` is not divisible by 2, we move on to the next number, which is 3. We continue this process until we find a prime factor, and then we divide `n` by that prime factor as many times as possible. The last remaining factor of `n` will be the largest prime factor.