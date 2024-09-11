```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    :param n: A number greater than 1
    :return: The largest prime factor of n
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

This script defines the `largest_prime_factor` function that finds the largest prime factor of a given number `n`. It does this by dividing `n` by increasing integers `i` as long as `n` is divisible by `i`. The loop continues until `i` squared is greater than `n`. At the end of the loop, `n` will be the largest prime factor of the original `n`.