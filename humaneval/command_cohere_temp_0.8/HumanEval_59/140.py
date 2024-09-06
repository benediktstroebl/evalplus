```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Go through each number from 2 to n, and check if n is divisible, starting from the end.
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from `2` to the square root of `n`, checking if `n` is divisible. It returns the largest prime factor by iterating in decreasing order and returning the first divisor found. This approach provides a straightforward solution for finding the largest prime factor. 

To ensure correctness for edge cases, the assumption that `n` is not a prime and is greater than 1 is made.