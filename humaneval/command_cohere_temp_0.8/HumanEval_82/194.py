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

The second function, `prime_length(string)`, takes a string as input and calculates the length of the string. It then calls the `is_prime()` function to determine whether this length value is prime. 

The code includes an ` isinstance()` check to make sure that the input `string` is a string, and returns `False` if it is not. 

Overall, this solution correctly determines whether the length of a given string is a prime number.