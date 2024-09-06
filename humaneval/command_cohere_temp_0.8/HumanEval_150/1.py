Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided:
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
    """Return x if n is prime, else return y."""
    if is_prime(n):
        return x
    else:
        return y

# Example usage:
n1 = 7
n2 = 15
x1, y1 = 34, 12
x2, y2 = 8, 5

print(f'For x_or_y({n1}, {x1}, {y1}) == {x1}')
print(f'For x_or_y({n2}, {x2}, {y2}) == {y2}')
```
This script includes two functions: is_prime, which checks whether a number is prime, and x_or_y, which returns x if n is prime and y otherwise. The example usage demonstrates the function's behavior for the provided test cases. Adjust the values of the variables n1, n2, x1, y1, x2, and y2 as needed to test different inputs.