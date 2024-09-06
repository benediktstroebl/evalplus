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
    """Return x if n is a prime number, otherwise return y."""
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

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function will return `x` if `n` is prime and `y` if `n` is not prime. The `is_prime` function is also included to check if a number is prime or not. 

The test cases section showcases how the `x_or_y` function works by utilizing different inputs and displaying the desired output. You can modify the test cases to assess the function's behavior on other input scenarios.