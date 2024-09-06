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
    """Return x if n is prime, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script includes a function `is_prime` that checks whether a given number is prime and returns `True` if it is. It returns `False` otherwise. The `x_or_y` function uses this functionality to return the value of `x` if the input `n` is prime, and `y` otherwise. The script also includes example usage that prints the output of the function for the two provided examples from the prompt. When the script is run, the output is:
```
34
5
```

This demonstrates that the script correctly solves the problem, as it returns `34` for the first example (as `7` is a prime number) and `5` for the second example (as `15` is not a prime number).  This solution is concise and self-contained, providing both the logic to determine primality and the functionality to solve the original problem in a single script.