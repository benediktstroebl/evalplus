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
    """Return x if n is prime, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script defines a function `x_or_y` that takes in three arguments: an input `n`, and values `x` and `y` and returns `x` if `n` is prime and `y` if it is not. The is_prime function is also included, which checks if a number is prime or not. Finally, the script includes test cases to verify the functionality of the `x_or_y` function. 

Note that the `is_prime` function utilizes an efficient algorithm, the `range` function has been optimized for the loop, and the prime checking is performed only up to the square root of the number. 

This code is efficient and effectively solves the problem while providing accurate results.