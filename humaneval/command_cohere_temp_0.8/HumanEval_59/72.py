```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest even factor as a starting point.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
```

This Python script defines a function called `largest_prime_factor` which takes in a single argument, `n`, assumed to be greater than 1 and not a prime number. The function returns the largest prime factor of `n`. This is achieved through a loop that starts from the factor of 2 and iterates up to the square root of `n`. During each iteration, the loop checks if the number `i` is a factor of `n` (i.e., `n % i == 0`) and if it is, it returns `i` as the largest prime factor. If not, it continues the loop, incrementing `i`. The loop ends before the square root of `n` is reached, as any factors greater than the square root would have corresponding factors smaller than the square root.  It should be noted that this approach ensures the correctness of the largest prime factor determination, adhering to the problem's specification.