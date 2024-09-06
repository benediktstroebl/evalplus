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
        x (int): Should be returned if n is prime.
        y (int): Should be returned if n is not prime.

    Returns:
        int: x or y depending on the primality of n
    """
    if is_prime(n):
        return x
    else:
        return y

# Tests
n1 = 7
x1 = 34
y1 = 12

n2 = 15
x2 = 8
y2 = 5

print(x_or_y(n1, x1, y1)) # Should print 34
print(x_or_y(n2, x2, y2)) # Should print 5
```

This script utilizes a simple primality test function to determine if the given number n is prime. The `x_or_y` function then returns the desired output based on this primality test, as per the problem's instructions. 

The tests in the script ensure that the function behaves correctly for the given input scenarios. You can add more tests to cover other cases and further verify the function's correctness.  If you encounter any issues or have further questions, feel free to ask!