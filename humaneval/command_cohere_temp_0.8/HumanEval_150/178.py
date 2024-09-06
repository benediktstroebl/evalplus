Here's a Python script that contains a function named `x_or_y` that solves the problem:
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

# Test cases
print(x_or_y(7, 34, 12))  # This should print 34
print(x_or_y(15, 8, 5))  # This should print 5
```

This script includes a `is_prime` function that checks if a number is prime. The `x_or_y` function then uses this to decide whether to return `x` or `y`. 

The test cases are printed to the console so you can see the function's behavior on those inputs. Let me know if you'd like me to explain any part of the code further!