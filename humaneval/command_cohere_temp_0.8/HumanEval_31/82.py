Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking for divisibility. If the number is divisible by any integer in that range, it returns `False`. If it isn't, it returns `True`.

This function is constructed to handle a wide range of inputs while maintaining a reasonable execution time. It does not rely on any external dependencies and efficiently determines the primality of the given number. 

You can use this function in conjunction with the provided tests to quickly verify its behavior. Simply copy the function into your code, and run the tests to see the expected outcomes. This allows you to immediately apply the function to your specific use case and determine if it satisfies your requirements.