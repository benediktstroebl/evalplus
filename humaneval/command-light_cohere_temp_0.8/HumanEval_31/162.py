Here is a Python script that passes the test cases provided:
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

This script defines a function `is_prime` that checks whether a given number `n` is a prime number or not. It uses some basic criteria along the the method, it first checks for numbers less than or equal to 3, then it checks for numbers that are divisible by 2 or 3, and then it uses a trial and error technique with the square of the number with itself and the square of double value of the number to check if the number is prime or not.