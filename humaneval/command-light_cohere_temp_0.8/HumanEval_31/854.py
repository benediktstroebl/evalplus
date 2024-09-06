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
The function is_prime determines whether a given number n is prime or not. It quickly checks various properties of numbers and returns True if the number is prime, and False otherwise. 

Note that the function is self-contained, and it can be used to check if a number is prime or not without calling other functions or using other parts of the code.