Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
This function, `is_prime()`, takes an integer `n` as input and checks whether it's prime or not. It uses some basic heuristic algorithms to determine primality, such as checking divisibility by 2 and 3, as well as testing divisibility by consecutive odd numbers up to the square root of n.