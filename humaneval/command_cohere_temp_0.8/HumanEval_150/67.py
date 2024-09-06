```python
def is_prime(n):
    """ Checks if a number is prime

    Args:
        n (int): Number to be checked

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Args:
        n (int): Number to be checked
        x (int): First integer choice
        y (int): Second integer choice

    Returns:
        int: x if n is prime, otherwise y
    """
    if is_prime(n):
        return x
    else:
        return y

# Tests
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
```

This script includes an `is_prime` function that accurately determines whether an integer is prime. The `x_or_y` function uses this functionality to return the value of `x` if `n` is prime, and `y` otherwise. 

The tests assert that the function behaves as expected, providing further confidence in its accuracy.