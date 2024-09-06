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
This function, `is_prime`, takes an integer `n` as input and checks whether it's a prime number. The function first handles basic cases where numbers are less than or equal to 2 and 3. Then, the function checks for divisibility up to sqrt(n) while incrementing a loop with value 6. This loop will run in a reasonable manner, as it avoids potential duplicates and checks divisibility by consecutive numbers.