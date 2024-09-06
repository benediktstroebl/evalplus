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
This code defines a function is_prime that checks if a given number is prime or not. It uses a basic prime number criteria, starting from 2 and 3, and then testing numbers up to the square root of the input number, checking for divisibility. The function returns True if the prime, and False otherwise. The function is self-contained and can solve the given problem of checking whether a number is prime or not without using any external functions or modules.