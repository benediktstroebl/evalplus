Here's a Python script that contains a function named `x_or_y` that fulfills the requirements mentioned in the markdown code block:
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

# Test cases
print(x_or_y(7, 34, 12))  # Output: 34
print(x_or_y(15, 8, 5))  # Output: 5
```

This script will output the correct results for the given test cases, namely `34` and `5`, respectively. 

The `is_prime` function is used to determine whether a number is prime. If the number is not prime, it returns `False`; otherwise, it returns `True`. The `x_or_y` function then uses this determination to decide whether to return `x` or `y`.