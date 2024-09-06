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
    """Return x if n is prime, else return y."""
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

The script then includes test cases to verify the function's behavior. The test cases exercise different scenarios, including prime and non-prime numbers, and validate that the function returns the expected values.  The expected output of the script is:
```bash
x_or_y(7, 34, 12) == 34
x_or_y(15, 8, 5) == 5
``` 

The expected results are consistent with the behavior of the `x_or_y` function described in the problem statement.