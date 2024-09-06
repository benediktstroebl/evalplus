```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print 34

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print 5
``` 

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is assumed to be prime or not), and two values `x` and `y`, and returns `x` if `n` is prime and `y` otherwise. It also includes tests that ensure the function behaves correctly for the given inputs. 

The `is_prime` function is also included, which employs a straightforward optimization to speed up the process of generating prime numbers. This function checks if a number is less than or equal to 3, returns `True` immediately. It then checks if the number is divisible by 2 or 3, and if so, returns `False`. It then starts from 5 and iterates through numbers 6k + 1 and 6k + 2 (i.e., 6, 11, 17, 23, 29, 37, ...) checking for divisibility. If the number is divisible by neither, it's prime. 

Overall, the code provides an efficient way of checking for prime numbers and extends it to solve the original problem of returning `x` or `y` depending on whether `n` is prime.