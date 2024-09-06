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
This function checks a given number `n` for primality. It begins by testing for numbers less than or equal to 2 and 3, which are acknowledged as prime numbers. The function then examines the testing by considering the value of the square root of the number and comparing it to the original number, and repeating this procedure until the square root of the number exceeds the original number. The function then returns true if no divisors are detected throughout the testing process.

This function is self-contained and can be used to check the primality of any given number.