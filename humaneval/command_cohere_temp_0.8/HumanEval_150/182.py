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

# tests
n = 7
x = 34
y = 12

print(f'for x_or_y({n}, {x}, {y}) == {x}')
assert x_or_y(n, x, y) == x

n = 15
x = 8
y = 5

print(f'for x_or_y({n}, {x}, {y}) == {y}')
assert x_or_y(n, x, y) == y
```

In the above code, the is_prime function checks if a number is prime or not. The x_or_y function then takes this into account to return the relevant value.