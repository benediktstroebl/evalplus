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

In the above code, the `is_prime` function is used to determine whether the number `n` is prime or not. If it is prime, the `x_or_y` function returns the value of `x`; otherwise, it returns the value of `y`.

The tests assert that the function `x_or_y` behaves as expected with the given inputs. You can modify the values of `n`, `x`, and `y` in the test blocks to see the function behaving as required.