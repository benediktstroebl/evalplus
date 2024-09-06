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
This function is designed to determine if a given number n is prime, meaning it has exactly two distinct positive divisors: 1 and n itself. The function utilizes an iterative approach to check for divisibility by square numbers up to the square root of n, while also considering the divisibility by multiples of 2 and 3.