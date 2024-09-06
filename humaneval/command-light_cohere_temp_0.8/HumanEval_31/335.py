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
This code defines a function `is_prime` that checks whether a given number `n` is prime or not. The function uses some simple heuristic tests to determine primality, including checking divisibility by 2 and 3, as well as other related prime numbers up to the square root of the number. It also incorporates a technique of iterating up the square root of the number while avoiding potential multiples of `i`.