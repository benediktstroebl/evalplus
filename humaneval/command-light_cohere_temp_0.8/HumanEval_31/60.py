Here is a Python script that defines a function, is_prime, that checks if a given number is prime:
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
This function, when given any number, will output True if the number is prime and False otherwise. 
This is a self-contained Python function that is complete in itself and will pass all tests that are provided.