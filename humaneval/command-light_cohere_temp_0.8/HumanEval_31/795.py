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
This code defines a `is_prime` function that checks whether a given number `n` is prime or not. The function uses basic primality criteria and checks divisibility conditions up to the square root of the number.

Note: The code assumes that the input `n` is a positive integer. This function will correctly identify prime numbers and false for non-prime numbers.