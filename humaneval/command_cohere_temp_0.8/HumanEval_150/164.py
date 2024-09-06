Here's a Python script that contains a function named `x_or_y` which returns either the value of `x` or `y` depending on whether the input `n` is a prime number or not:
```python
def is_prime(n):
    """Function that checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    """
    if is_prime(n):
        return x
    else:
        return y

# Adding tests to the function
def test_x_or_y():
    """Tests for x_or_y function."""
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5
    assert x_or_y(2, 21, 14) == 21
    assert x_or_y(4, 101, 42) == 42

test_x_or_y()
```

In the above code, the `is_prime` function is used to check if `n` is a prime number. If it is, the `x_or_y` function returns `x`, otherwise it returns `y`. The `test_x_or_y` function provides tests for the `x_or_y` function, it calls the function multiple times with different inputs and compares the output with the expected values using Python's `assert` statement. 

The use of `assert` allows for the automatic checking of preconditions and postconditions as the program will raise an error if these conditions are not met. Thus, we ensure that the function always behaves as expected.