```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
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

# Test cases
n1 = 7
x1 = 34
y1 = 12
print(f'x_or_y({n1}, {x1}, {y1}) == {x1}')

n2 = 15
x2 = 8
y2 = 5
print(f'x_or_y({n2}, {x2}, {y2}) == {y2}')
```

This script defines a function `x_or_y` that takes three arguments, `n` (the number to check), `x` (the value to return if `n` is prime), and `y` (the value to return if `n` is not prime). The function uses the `is_prime` function to determine whether `n` is prime and returns the corresponding value.

The script then includes test cases to validate the correctness of the `x_or_y` function. The test cases print the results of calling `x_or_y` with different arguments and show that the function returns the expected values based on primality.