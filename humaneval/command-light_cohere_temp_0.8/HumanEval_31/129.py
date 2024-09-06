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
This function, named **is_prime**, accepts an integer **n** as input and outputs a boolean indicating whether **n** is a prime number or not. It uses some basic and efficient algorithms to determine primality, such as checking divisibility by 2 and 3, and then using a simple loop to identify other prime numbers up to the square root of 2.