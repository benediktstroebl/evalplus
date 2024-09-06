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

The function `is_prime_length` is a utility function that checks whether a given number is prime or not. It's used by the `prime_length` function, which takes a string and returns a boolean indicating whether the length of the string is a prime number. The script passes the test cases provided in the prompt. You can use it to test more strings as well.