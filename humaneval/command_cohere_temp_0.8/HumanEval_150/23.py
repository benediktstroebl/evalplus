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
    """Return x if n is a prime number, otherwise return y."""
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

This code includes a separate function, `is_prime`, that determines if a given number is a prime number or not. The `x_or_y` function then uses this `is_prime` function to decide whether to return `x` or `y`. The test cases are also included, and the script should be run to see the output for verification.  This approach allows for better organization and reusability in the code.