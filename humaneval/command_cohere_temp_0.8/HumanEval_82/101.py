```python
def is_prime_length(length):
    """Verifies if a given length is a prime number or not"""
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    """
    return is_prime_length(len(string))
```

This script defines a function `prime_length` which takes a string and returns a boolean indicating whether the length of the string is a prime number or not. It includes a separate function `is_prime_length` that verifies a given length is a prime or not, which is later used by the `prime_length` function. 

The script passes the test cases provided in the prompt:
```
> prime_length('Hello')
True

> prime_length('abcdcba')
True

> prime_length('kittens')
True

> prime_length('orange')
False
``` 
It's a self-contained script that fulfills the problem statement.