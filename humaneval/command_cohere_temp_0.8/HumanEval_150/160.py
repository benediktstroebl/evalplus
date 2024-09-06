```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "34"

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print "5"
``` 

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is presumed to be either prime or non-prime), and two values `x` and `y` (values to be returned depending on the primality of `n`). It then uses the `is_prime(n)` function to determine whether `n` is prime; if so, it returns `x`, and otherwise, it returns `y`. This is specified in the function docstring.

The script also includes tests for the `x_or_y` function, which verify that the function returns the expected results for two different test cases. 

To see the full power of the `is_prime` function, you might consider a more comprehensive test: `is_prime(n)` should return `True` for 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, whereas it should return `False` for all other numbers less than 100.