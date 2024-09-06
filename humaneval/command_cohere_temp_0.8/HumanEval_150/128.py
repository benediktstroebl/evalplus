Here's a Python script with a self-contained function that solves the problem and passes the tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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

This code defines a function `x_or_y` that takes three arguments: an input number `n`, and two optional parameters `x` and `y`. The function returns `x` if `n` is prime and `y` if `n` is not prime. The code also includes a separate function `is_prime` which is a simple prime-checking function. 

The code outputs the correct values for the example inputs in the original prompt (`34` for `7` and `5` for `15`). 

Let me know if this solution works for you or if you need anything else!