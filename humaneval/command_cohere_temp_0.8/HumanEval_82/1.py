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

The function `is_prime_length` is a utility function that checks whether a given length is prime. This function is used by `prime_length` to check whether the length of the input string is a prime number. The function returns True if the string length is a prime number and False otherwise.

This approach allows for a more concise and reusable solution to the problem, as the logic for checking primality is encapsulated in a separate function that can be used in other parts of the code as well.