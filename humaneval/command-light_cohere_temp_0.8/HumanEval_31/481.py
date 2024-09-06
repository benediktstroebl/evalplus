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
This code defines a function 'is_prime' which takes an integer 'n' as input and checks whether it's prime or not. It uses a provided test to find divisibility of numbers and determine if it's prime or not. 

Would you like to explore other features or functionalities of Python, or discuss different programming concepts?