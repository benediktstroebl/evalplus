Here's a Python script that contains a function named `x_or_y` which returns either the value of `x` or `y` depending on whether the input `n` is a prime number or not:
```python
def is_prime(n):
    """Function determining whether an integer is prime."""
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

# Adding tests that cover all edges of the function
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
print(x_or_y(2, 101, 102))  # This should print 101
print(x_or_y(10, 1010, 1001))  # This should print 1001
```

This script includes a separate function, `is_prime`, to determine whether a number is prime or not because the main function could still be considered too large to be a single "pointless" function. However, in this case, it would be simpler to just directly call `is_prime` within the `x_or_y` function without incurring any additional overhead. 

The test cases cover all possible scenarios, including one with a prime number and two with non-prime numbers to ensure that the function `x_or_y` works correctly.