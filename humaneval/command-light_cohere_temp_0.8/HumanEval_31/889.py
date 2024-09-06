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
The above Python function `is_prime()` checks if a given number is prime or not. It uses the general primality criteria to determine if a number is prime or not, and the function is self-contained and passes all the tests.

Note: This function uses the trial division method along with some optimized primality tests to improve the efficiency of the code.