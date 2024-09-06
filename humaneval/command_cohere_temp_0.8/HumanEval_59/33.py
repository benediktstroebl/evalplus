```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest odd factor
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    # If no odd factor is found, the largest factor is 2
    return 2
```

This Python script defines a function called `largest_prime_factor` which takes in a single argument, `n`, assumed to be greater than 1 and not a prime number. The function returns the largest prime factor of the given number 'n'. It does this by first checking if the odd factors between 3 and `n**0.5` divisible `n`. If it finds one, it returns it. If not, it returns 2, the largest prime factor. This is done using standard mathematical factoring knowledge and is efficient for its purpose.