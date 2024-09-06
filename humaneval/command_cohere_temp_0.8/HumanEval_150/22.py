Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the markdown code block:
```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Examples:
# x_or_y(7, 34, 12) == 34
# x_or_y(15, 8, 5) == 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose values should be switched depending on the primality of `n`. The code also defines a helper function `is_prime` to check if a number is prime. The `x_or_y` function uses the `is_prime` function to determine whether `n` is prime and returns the appropriate value (`x` or `y`) based on this determination. The example tests are also provided and should return the expected values.