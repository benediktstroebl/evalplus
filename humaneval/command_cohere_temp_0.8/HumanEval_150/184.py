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
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print True

n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}') # Should print True
``` 

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is assumed to be either prime or non-prime), and two values `x` and `y` (which should be returned depending on the primality of `n`). The script also includes a function `is_prime(n)` that checks if a number is prime. Finally, it includes two example tests that demonstrate the behavior of the `x_or_y` function. 

To ensure that the `x_or_y` function behaves correctly, the `is_prime` function is utilized. This function determines whether a given number `n` is prime or not. It first handles the case when `n` is less than 2, returning `False`. Then, it loops through numbers from 2 to the square root of `n` (inclusive), checking whether `n` is divisible by any of them. If `n` is divisible by any of these numbers, it returns `False`. However, if no divisors are found, it confirms that `n` is prime by returning `True`. 

By using `is_prime(n)` within the `x_or_y` function, the behavior of the problem statement is accurately replicated. When `n` is prime, the function returns `x`, and when `n` is not prime, it returns `y`.