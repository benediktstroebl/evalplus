```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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
print(f'x_or_y({n}, {x}, {y}) == {x}: {x_or_y(n, x, y) == x}')
n = 15
x = 8
y = 5
print(f'x_or_y({n}, {x}, {y}) == {y}: {x_or_y(n, x, y) == y}')
```

The `is_prime` function is introduced to encapsulate the primality test behavior, allowing for more robust and understandable code. This approach makes the code easier to maintain and promotes modularity, as the primality check and the decision-making logic are separated into distinct functions.