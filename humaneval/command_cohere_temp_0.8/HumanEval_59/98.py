```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor first. This avoids wasting efforts on multiples.
    max_divisor = n // 2
    for divisor in range(3, int(n**0.5) + 1, 2):
        while n % divisor == 0:
            n //= divisor
        if n == 1:
            return divisor
    if n > 1:
        return n
```
The approach is optimized based on the fact that prime factors tend to appear near the largest factor of a number. The loop starts from 3, progressing in steps of 2, it checks all potential divisors of odd numbers. For even numbers, it's the job of the while loop to strip away all respective divisors. Finally, if there is anything left of the number, it is returned as the largest prime factor.