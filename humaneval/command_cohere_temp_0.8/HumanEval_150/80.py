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

This script defines a function `x_or_y(n, x, y)` that takes three arguments, `n` (which is assumed to be either prime or non-prime), and two values `x` and `y` (which should be returned depending on the primality of `n`). The script also creates two tests to validate the functionality of the `x_or_y` function.

Note that the function `is_prime(n)` is a simple primality-checking function that only accepts integers. If the integer is less than 2, it returns false. It then iterates through integers from 2 to `sqrt(n)` and checks if n is divisible by any of them. If it is, it returns false. If it isn't, it returns true. This function is not foolproof, and many edge cases will fail. Let me know if you'd like to expand on this function to make it more robust.