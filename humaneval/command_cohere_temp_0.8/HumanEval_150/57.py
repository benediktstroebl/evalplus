Here's a Python script with a self-contained function that solves the problem and passes the tests:
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

# Example usage
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function behaves differently depending on whether `n` is prime: it returns `x` if `n` is prime and `y` otherwise. To determine whether a number is prime, it uses an efficient algorithm that checks only the smallest prime divisors. Feel free to test it with different inputs.