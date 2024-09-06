Here's a Python script with a self-contained function that solves the problem and passes the tests:
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
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes in three arguments: an input number `n`, and two optional parameters `x` and `y`. The function returns `x` if `n` is prime and `y` if `n` is not prime. The `is_prime` function is also included to correctly determine whether a number is prime or not. 

The test cases at the end demonstrate the correct behavior of the `x_or_y` function for the given inputs. 

Note that this script assumes that the input values meet the requirements specified in the prompt, namely, that `n` is a positive integer, and that `x` and `y` are not `None` or `False`, and that `x` is not necessarily equal to `y`.