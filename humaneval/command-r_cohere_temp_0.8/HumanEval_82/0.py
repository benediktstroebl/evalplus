```python
def prime_length(string):
    """Returns True if the length of the string is a prime number, False otherwise."""
    length = len(string)
    for num in range(2, length):
        if length % num == 0:
            return False
    return True
```