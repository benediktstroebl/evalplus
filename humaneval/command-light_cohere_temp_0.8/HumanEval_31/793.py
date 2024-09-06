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
This code defines a function 'is_prime' that checks if a given number 'n' is prime. It uses an iterative approach to check divisibility of numbers up to the square root of 'n' to determine primality. The function first checks small numbers and returns 'False' if the number is not prime, and 'True' if it is prime.