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
This code defines a function `is_prime` that checks whether a given number is a prime. The function first checks for numbers less than or equal to 1 and returns `False`. Then, it checks for numbers less than or equal to 3 and returns `True`. Next, it checks for the numbers that are divisible by 2 or 3 using the modulo concept. After that, the function starts checking for numbers greater than 3 using the `i` variable, which is initially set to 5. Then, the function checks for divisibility by smaller powers of `i` until the square root of `i` exceeds the given number.  Finally, the function returns `True` if the condition holds.