### Largest Prime Factor

The following Python script defines a function `largest_prime_factor` to find the largest prime factor of a given number `n`.

```markdown
### largest_prime_factor.py
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.

    Args:
    n (int): A number greater than 1, not a prime.

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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

### How it works

1.  Initialize a variable `i` to 2, which is the smallest prime number.
2.  Enter a while loop that continues as long as `i` squared is less than or equal to `n`.
3.  Inside the loop, check if `n` is divisible by `i` using the modulus operator (`%`). If it's not divisible, increment `i` by 1 to check the next potential factor.
4.  If `n` is divisible by `i`, divide `n` by `i` to reduce it and repeat the process.
5.  Once the loop ends, `n` will be the largest prime factor of the original number.

This approach takes advantage of the fact that a larger factor of `n` must be a multiple of a smaller factor that has already been checked, thus reducing the number of iterations required to find the largest prime factor.