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
```

The `is_prime` function is used to determine if a number is prime. If the number is prime, the `x_or_y` function returns its corresponding 'x' value. If the number is not prime, the function returns its corresponding 'y' value. 

The example output for the given test will be:
```
x_or_y(7, 34, 12) == 34
```

The script passes the test as the function returns `34` for the input `x_or_y(7, 34, 12)`.