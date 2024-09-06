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
This function checks a number `n` for primality, it uses some basic divisibility rules and trial division to efficiently determine if the number is prime or not. 
The function is self-contained, and it passes all the test cases provided in the original prompt.