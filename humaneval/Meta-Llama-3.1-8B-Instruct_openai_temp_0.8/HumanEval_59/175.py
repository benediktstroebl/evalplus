### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.

    Args:
    n (int): A number greater than 1 that is not a prime.

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
This function works by dividing the input number `n` by increasing integers `i` until it finds a divisor. It uses a while loop to keep track of `n` and `i`. If `n` is divisible by `i`, `n` is divided by `i`. If `n` is not divisible by `i`, `i` is incremented. The loop continues until `i` is greater than the square root of `n`, at which point `n` must be a prime number (its only factor being 1 and itself). The function then returns `n`, which is the largest prime factor of the original number.

This approach ensures that the function runs efficiently even for large inputs, with a time complexity of O(sqrt(n)).