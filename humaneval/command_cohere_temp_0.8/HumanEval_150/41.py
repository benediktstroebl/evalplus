```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is presumed to be either prime or non-prime), and two values `x` and `y` (which should be returned depending on the primality of `n`). It also contains a helper function, `is_prime(n)`, which checks if a number is prime. This function is used to determine whether `n` is prime. Ultimately, the `x_or_y` function returns `x` if `n` is prime and `y` otherwise. 

The last part of the script includes some tests that verify the function behavior against the expected one. The script should print "34" and then "5" as each test verifies the correctness of the function against the given examples from the prompt.  Overall, the script solves the problem posed in the prompt and demonstrates the use of a primality test in Python.