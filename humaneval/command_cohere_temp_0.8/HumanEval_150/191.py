Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests:
```python
def is_prime(n):
    """ Checks if a number is prime """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """ Returns x if n is prime, else returns y """
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12

if x_or_y(n, x, y) == x:
    print("Pass")
else:
    print("Fail")

n = 15
x = 8
y = 5

if x_or_y(n, x, y) == y:
    print("Pass")
else:
    print("Fail")
```

This script includes a `is_prime` function that tests if a number is prime and returns `True` if it is, and `False` otherwise. The `x_or_y` function is polled with two sets of arguments, and accordingly, it should return `34` for the first case and `5` for the second. The script then verifies if these outputs are correct, and prints "Pass" in case of correctness, and "Fail" otherwise.