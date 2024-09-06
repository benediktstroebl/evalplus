```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function returns `x` if `n` is prime and `y` if `n` is not prime. 

The script also includes a test function `is_prime` which is used to validate the `x_or_y` function. 

The two printed statements at the bottom demonstrate the correct behavior of the program.