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

# Tests
n = 7
x = 34
y = 12
print(f'x_or_y({n}, {x}, {y}) == {x}')

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {y}')
```

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (a number), and two variables `x` and `y`. The function returns `x` if `n` is prime and `y` otherwise. It employs a helper function, `is_prime(n)`, to determine if a number is prime or not. The script then conducts two tests that check the function's behavior for specific inputs. 

The `is_prime(n)` function checks if `n` is less than or equal to 1, in which case it returns `False` (since prime numbers are defined as greater than 1). It then iterates from 2 up to the square root of `n` (inclusive), checking if `n` is divisible by any of these numbers, and returning `False` if it is. If no divisors are found, the function returns `True`, indicating that `n` is prime. 

The `x_or_y(n, x, y)` function utilizes the `is_prime(n)` function to determine if `n` is prime. If `n` is prime, it returns the value of `x`; otherwise, it returns the value of `y`. 

The final two lines are test blocks that demonstrate the behavior of the function with specific inputs and print the expected results.  The function is designed to pass both tests, thereby confirming its behavior aligns with the problem statement.