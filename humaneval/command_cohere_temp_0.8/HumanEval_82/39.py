```python
def is_prime_length(length):
    """
    Returns True if the given length is prime, else False.
    """
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
    if is_prime_length(len(string)):
        return True
    else:
        return False
```

The function `prime_length` uses the helper function `is_prime_length`, which tests whether a given length is prime. This is done by iterating from 2 to the square root of the target length, and checking if the length is divisible by any number in that range. The `prime_length` function then uses this helper function to check whether the length of the input string is prime, and returns True if so.

This code will correctly determine whether the length of an input string is a prime number, based on the provided string lengths in the example cases.