### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
    n (int): The input number. Must be greater than 1 and not prime.

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

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a loop to check divisibility of `n` by increasing integers starting from 2. If `n` is divisible by `i`, it divides `n` by `i` and continues the loop. If `n` is not divisible by `i`, it increments `i` by 1 and continues the loop. The loop continues until `i` squared is greater than `n`. The remaining value of `n` is the largest prime factor.

When you run this script, it prints the largest prime factor of 13195 (29) and 2048 (2).