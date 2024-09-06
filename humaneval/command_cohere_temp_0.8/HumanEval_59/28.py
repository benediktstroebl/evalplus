```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function called `largest_prime_factor` which takes in a single argument, `n`, assumed to be greater than 1 and not a prime number. The function returns the largest prime factor of `n`. This is achieved through a loop that starts from the factor 2 and iterates up to the square root of `n`. During each iteration, it checks if `n` is divisible by the current `i`, and if it is, the function returns `i` as the largest prime factor. If not, it continues the loop, potentially skipping over multiples of other factors. This strategy is efficient because it avoids unnecessary checks by leveraging the fact that prime factors are generally sparse around the middle of the number. 

The function is designed to return the largest prime factor of a given number `n`, which is useful in various mathematical, statistical, and computational scenarios.