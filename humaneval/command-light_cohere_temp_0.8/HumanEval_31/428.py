```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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
The function checks whether a given number is prime or not. It uses a prime numbers testing methods: division by 2 and 3, and factoring by consecutive squares. 

The function is designed to be self-contained, using only a limited set of inputs and a few simple rules. 

To pass all the tests, you can simply call the function with the input values and compare the returned values.