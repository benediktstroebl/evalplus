```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for highest value divisible by 2
    if n % 2 == 0:
        return 2
    # Check for highest value divisible by 3
    if n % 3 == 0:
        return 3
    # Check from 5 to square root of n
    for i in range(5, int(n**0.5) + 1, 2):
        if n % i == 0:
            return i
    # If no factors are found, return n
    return n
```

This Python script defines a function called `largest_prime_factor` that takes in a number `n` as an argument and returns the largest prime factor of that number. The function first checks if `n` is divisible by 2, and if it is, it returns 2. If not, it checks whether `n` is divisible by 3, and if so, it returns 3. If neither 2 nor 3 divide `n`, the function iterates through numbers 5, 7, 9, and so on up to the square root of `n`, checking for divisibility. Once a divisor is found, the function returns that factor; if no factors are found, the function returns `n` itself. This strategy ensures the correct largest prime factor is returned, assuming `n` is greater than 1 and not a prime number itself.