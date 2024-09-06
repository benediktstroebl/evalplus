Here's a Python script with a self-contained function that solves the x_or_y problem and passes the tests provided in the prompt:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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

This script defines a function `x_or_y` that takes three arguments: an input number `n`, and two values `x` and `y` whose return is desired based on the prime-ness of `n`. The function utilizes the `is_prime` function to determine whether `n` is prime and returns `x` if it is, and `y` otherwise. 

The `is_prime` function checks if a given number `n` is less than or equal to 1, in which case it returns `False`. If `n` is 2 or 3, it returns `True` since these are prime numbers. Alternatively, if `n` is an even number except for 2, or a multiple of 3, then it returns `False`. The loop starts from 5, checking through the odd numbers less than or equal to the square root of `n`. If none of these divide `n`, it is prime, otherwise, it is not. 

The script also includes example usages of the `x_or_y` function to verify its behavior.