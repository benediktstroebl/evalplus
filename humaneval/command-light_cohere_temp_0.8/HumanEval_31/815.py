Here is a Python script with a self-contained function that solves the problem and passes the tests:

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

This function uses a combination of tests to determine whether a given number n is prime or not, including square and twin factors. It will correctly identify prime numbers and correctly indicate non-prime numbers, making it a self-contained function.