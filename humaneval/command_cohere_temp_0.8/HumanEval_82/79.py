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

This code defines a function `is_prime(num)` that checks whether a given number is prime or not. It then uses this function to check if the length of the input string is a prime number or not, depending on whether it's an integer or not, and returns the corresponding boolean value.

The `prime_length` function defines the behavior described in the code block, utilizing the previously defined `is_prime` helper function to check if the length of a given string is a prime number. 

This Python script efficiently solves the problem and fulfills the requirement specified in the given code block. It provides a self-contained function that can be reused later easily. 
If you want to elaborate more on this solution or test more cases for the `prime_length` function, feel free to ask!