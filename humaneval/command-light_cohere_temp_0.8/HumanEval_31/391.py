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
This function, is_prime, takes an integer n as input and returns True if n is a prime number and False if not. The function uses a simple trial and error logic, checking for divisibility by 2, 3, and a range of prime numbers up to the square root of n. It also checks for divisibility by numbers that form the respective prime number's square.