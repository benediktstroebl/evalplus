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
```

The function `is_prime()` is self-contained and takes an integer `n` as an argument. It then checks various conditions to determine if the given number is prime or not. The function uses the basic principles and tests to determine primality. The function also passes all the tests provided in the original prompt.