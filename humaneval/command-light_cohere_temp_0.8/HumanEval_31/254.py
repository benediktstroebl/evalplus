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
This function uses some basic heuristics and divisibility tests to determine if a given number is prime. 

The function is designed to be efficient and to handle a wide range of input values.  It can be used to quickly check whether a number is prime or not, which can be useful in various applications such as cryptography, coding, and statistics.