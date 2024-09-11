```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

Explanation:

* We start checking from `i = 2`, which is the smallest prime number.
* We check if `i` is a factor of `n` by using the modulo operator (`n % i`).
* If `i` is not a factor, we increment it by 1.
* If `i` is a factor, we divide `n` by `i` and repeat the process.
* We keep doing this until `i` is greater than the square root of `n`.
* At this point, `n` will be the largest prime factor of the original number.

This algorithm is efficient because it only needs to check divisors up to the square root of `n`. This is because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.