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
This function is_prime checks whether a given number is prime or not. It uses a specific rules and condition to determine if a number is prime or not, using the `if-else` statement and `while` loop. The tests cover different numbers from 2 up to the square root of the number, ensuring a proper check.