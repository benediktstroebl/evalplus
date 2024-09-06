```python
def is_prime_length(length):
    if length <= 1:
        return False
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
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
    return is_prime_length(len(string))
```

The function `is_prime_length` is a utility function that takes an integer and checks if its prime. The function `prime_length` takes a string and returns a boolean indicating whether the length of the string is a prime number. It utilizes the `is_prime_length` helper function to perform this check.