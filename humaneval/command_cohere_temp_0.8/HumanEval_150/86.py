Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the prompt:
```python
def is_prime(n):
    """ Checks if a number is prime

    Args:
        n (int): Number to be checked

    Returns:
        bool: True if n is a prime number, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is a prime number and should return the value of y otherwise.

    Args:
        n (int): Number to be checked
        x (int): First integer
        y (int): Second integer

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

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The purpose of this function is to return `x` if `n` is prime, and `y` if `n` is not prime. The `is_prime` function is used to determine whether a number is prime. It's a simple brute-force approach to check for primality, where it iterates from 2 to the square root of the number, checking for any divisors. 

The tests provided in the prompt are also included to ensure the function behaves as expected. The code will output `True` for both test cases, indicating that the function correctly solves the problem.  This approach has a time complexity of O(sqrt(n)), where `n` is the number to be checked for primality. While this is a simple and straightforward solution for checking primality, it is not the most efficient approach for larger numbers. 

This code demonstrates a basic use of Python to solve a problem that involves primality testing, and it can serve as a foundational example for understanding how to check for primality and extend this functionality to other more complex problems or requirements. 

You can use this code as a starting point and ensure that you understand each part of the code and how it works, and then modify it to tailor it to your needs.