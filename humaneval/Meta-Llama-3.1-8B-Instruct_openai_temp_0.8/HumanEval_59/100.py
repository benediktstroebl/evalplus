```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    :param n: The input number.
    :return: The largest prime factor of n.
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

This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of the input number `n`. It iteratively checks for divisibility by increasing integers `i`, starting from 2, and updates `n` by dividing it by `i` whenever it finds a divisor. The loop continues until `i` is larger than the square root of `n`, at which point `n` is guaranteed to be prime. The function finally returns `n`, which is the largest prime factor.