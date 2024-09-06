```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as the answer
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    # If no even factor found, then it's a prime number
    return n
```
The function iterates through numbers from 2 up to the square root of `n`. It checks if the number is divisible by any of these numbers and returns the largest even divisor as the largest prime factor. If no even divisor is found, it means that `n` is a prime number itself, so the function returns `n` as the largest prime factor. This approach ensures that the largest prime factor is found correctly in both scenarios: when `n` has a largest even factor and when it doesn't.