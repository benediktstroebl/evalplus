```python
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not isinstance(string, str):
        return False
    return is_prime(len(string))
```

This code defines a function `is_prime(num)` that checks whether a given number is prime or not. It then uses this function to check if the length of the input string is a prime number or not, depending on whether it's a string or not. The `prime_length` function takes a string as input and returns True if the string's length is a prime number, and False otherwise. 

The `prime_length` function first checks if the input is a string with `isinstance(string, str)`. It then uses the `is_prime` function to check if the length of the string is prime.