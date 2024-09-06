Here's a self-contained Python function that checks whether a given number is a prime or not:
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
This function takes an integer `n` as input and returns `True` if `n` is a prime, and `False` otherwise. It uses a different basic and efficient approach to find whether a given number is prime or not using the `mod` operator, divisibility rules, and the sqrt function. 

This function is self-contained and does not rely on any external functions or modules, making it a concise and efficient solution for the given problem.