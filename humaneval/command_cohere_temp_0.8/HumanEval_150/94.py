Here's a Python script with a self-contained function that solves the problem and passes the tests:
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
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```
This script defines a function `x_or_y` that takes three arguments: `n` (a numeric value), `x` (the value to return if `n` is prime), and `y` (the value to return if `n` is not prime). The function utilizes an auxiliary function `is_prime` to determine whether a number is prime or not. The `is_prime` function iterates through the numbers from 2 to the square root of `n`, if it finds any divisors, it returns `False`, and if not, it confirms that `n` is prime.

The script also includes test cases to verify the function's behavior. You can add more test cases to cover a wide range of prime and non-prime numbers for more comprehensive testing.