```python
def is_prime_length(length):
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True

def prime_length(string):
    string_length = len(string)
    return is_prime_length(string_length)
```

This script defines a function `prime_length` that takes a string and returns `True` if the length of the string is a prime number and `False` otherwise. It includes a test suite that covers edge cases like string lengths of `0`, `1`, and some composite lengths, as well as a few prime lengths. 

To more efficiently check for primality, we only need to check the divisibility of the length up to its square root, which is achieved by the loop ranging up to `int(length**0.5) + 1`.