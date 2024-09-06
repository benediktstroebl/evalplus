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

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
assert x_or_y(n, x, y) == x

n = 15
x = 8
y = 5

print(f'x_or_y({n}, {x}, {y}) == {x_or_y(n, x, y)}')
assert x_or_y(n, x, y) == y
```

In the above code, the `is_prime` function checks if a number is prime or not. It employs a straightforward algorithm: iterating from 2 to the square root of the number, it checks whether the number is divisible by any integer in that range. If the number is divisible by any, it immediately returns `False`, indicating that the number is not prime. Otherwise, it returns `True`.

The `x_or_y` function utilizes the `is_prime` function to solve the problem. If `n` is prime, it returns `x`, otherwise it returns `y`.

The code includes simple tests to validate the correctness of both functions. It prints out the result of calling `x_or_y` with various arguments and asserts that the output is as expected. 

By running this code, you can observe the test failures (if the assert statements are not met) or confirm that the functions operate as described. You can also integrate these functions into larger programs to solve specific prime number problems as needed.