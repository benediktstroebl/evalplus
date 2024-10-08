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
    """
    if not isinstance(string, str):
        return False
    return is_prime(len(string))
```

This script defines a function `is_prime(x)` that checks whether a given number `x` is prime. It iterates through numbers from 2 to the square root of `x`, checking for divisibility. If the number is divisible by any integer within this range, it's not prime; otherwise, it is prime. 

The second function, `prime_length(string)`, takes a string as input and uses the `is_prime` function to determine whether the length of the string is prime. If the length is not a prime number, the function returns `False`, and if it is a prime number, the function returns `True`. This function also validates that the input `string` is a string. 

Therefore, this code passes all test cases:
- `prime_length('Hello')` returns `True` because the length of the string `"Hello"` is a prime number. 
- `prime_length('abcdcba')` returns `True` because although the string contains duplicates, its length is still a prime number. 
- `prime_length('kittens')` returns `True` for the same reason. 
- `prime_length('orange')` returns `False` because the length of the string `"orange"` is not a prime number. 

Overall, the code demonstrates a straightforward approach to testing primality in Python.