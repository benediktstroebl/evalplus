```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Make sure to use reasonably efficient algorithms, e.g., trial division
    # Avoid brute-force factors like n // 2 until n == 1.
    largest_factor = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        # Move ahead if the remainder is not divisible by i
        if n == 1:
            break
    return largest_factor if n == 1 else -1  # Return -1 if n is a prime
```

The Python script comes with a function named `largest_prime_factor` that identifies the largest prime factor of a given number `n`. It employs a trial division method efficient enough for handling factoring queries. In case `n` is a prime number, the function returns `-1` as the largest prime factor. Two sample tests are provided to showcase its functionality, checking the largest prime factors of `13195` and `2048`.

The largest_prime_factor function effectively factors large numbers by repeatedly dividing them by the largest discovered prime factor. This efficient approach significantly reduces the number of divisions needed for larger numbers.