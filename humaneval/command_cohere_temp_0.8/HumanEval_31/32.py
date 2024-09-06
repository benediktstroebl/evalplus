```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, employing a checking mechanism that iterates through factors up to the square root of the number. It ultimately returns 'True' if the number is prime and 'False' if it is not. This method is efficient for its purpose and showcases the simplicity and practicality of Python for such problems.