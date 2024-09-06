```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor
    max_factor = n - 1
    while max_factor % 2 == 0:
        max_factor //= 2
    for possible_factor in range(3, int(n ** 0.5) + 1, 2):
        while n % possible_factor == 0:
            n //= possible_factor
            if n == 1:
                return possible_factor
    return n
```
The largest possible factor of `n` is `n - 1`, which obviously divides `n`. If `n - 1` is even, it must be divisible by 2. The loop splits `n` into smaller and smaller odd factors until it finds a prime.

The loop that iterates through `range(3, int(n ** 0.5) + 1, 2)` avoids even numbers and progressively narrows down possible factors by dividing `n` with them. If a divisor is found, it divides `n` by it and continues the process until it reaches 1, at which point it returns the last divisor as the largest prime factor. If no divisors are found in this range, it assumes `n` must be a prime itself, which is technically also valid according to the problem statement, and returns `n`.