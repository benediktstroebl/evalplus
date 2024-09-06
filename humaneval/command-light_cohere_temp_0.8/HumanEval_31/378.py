Here is a Python script with a self-contained function that checks whether a given number is prime or not:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.0 / 2) + 1):
        if n % i == 0:
            return False
    return True
```

This script defines a function `is_prime` that checks whether a given number `n` is prime or not. It uses a specific condition to determine if a number is less than or equal to 1, which means it's not prime, and then it iterates through numbers from 2 up to the square root of the input number `n` and checks for divisibility. The function returns `True` if the input number is prime, and `False` otherwise.