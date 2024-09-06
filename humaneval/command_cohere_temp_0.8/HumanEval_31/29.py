Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns `False`. Otherwise, it returns `True`.

This code assumes that the tests will be run directly in the same file or that the function is used in the context of an interactive Python session, where the tests can be executed separately. The function's behavior is in accordance with the test cases provided in the original prompt.