Here's a Python script with a self-contained function that solves the problem and passes the tests:
```python
def is_prime(n):
    """ Checks if a number is prime

    Args:
        n (int): Number to check if it is prime

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
    """ A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Args:
        n (int): Number to base the return value on.
        x (int): One of the values to return.
        y (int): The other value to return.

    Returns:
        int: x if n is prime, otherwise y.
    """
    if is_prime(n):
        return x
    else:
        return y

# Tests
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
```

This script includes a `is_prime` function that checks if a given number is prime. It also includes the `x_or_y` function that solves the original problem and demonstrates this with a test suit that checks the functionality of the program with different inputs and expected outputs. 

Note, the `is_prime` function could be optimized as it checks for primality by iterating through every number up to the square root of the target number. This is the classical approach to checking for primality and does have a linear time complexity O(n). There are more efficient methods to check for primality that are based on number theory such as the ones provided here: https://www.geeksforgeeks.org/prime-numbers-using-python-special-functions/