```python
def is_prime_length(s):
    """Returns True if the length of the input string is a prime number, else False"""
    if len(s) <= 1:
        return False
    for i in range(2, int(len(s)**0.5) + 1):
        if len(s) % i == 0:
            return False
    return True
```

The function `is_prime_length()` takes a string `s` as input and returns True if the length of the string is a prime number and False otherwise. The function first checks if the length of the string is less than or equal to 1, returning False in such cases as strings of length 0 or 1 are not prime. It then iterates from 2 up to the square root of the string length, checking if the length of the string is divisible by any number in this range. If it is, it returns False, indicating that the length is not a prime. If it isn't, it returns True, indicating that the length is a prime.

This approach optimizes the prime-checking process by only focusing on integers that have a realistic chance of being factors of the target length, reducing the number of checks needed.