Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the prompt:
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

In this script, the `is_prime` function is used to determine whether a number is prime or not. If the number is prime, the `x_or_y` function returns the value of `x`; otherwise, it returns the value of `y`. The script also includes example usages that demonstrate the function's behavior for the provided test cases. 

This code is self-contained and does not rely on any external variables or contexts, making it easy to reuse and test independently.