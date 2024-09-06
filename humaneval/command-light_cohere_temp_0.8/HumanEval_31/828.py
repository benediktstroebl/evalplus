Here is a Python function that checks if a number is prime:
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
```
This function will determine whether a given number is prime, and will return a boolean value (True or False) accordingly. 
It uses a simple algorithm to check for divisibility, starting from 2 and going up to the square root of the number.