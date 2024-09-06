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

This script defines a function `is_prime(num)` that checks whether a given number is prime or not. It employs a simple optimization by checking only up to the square root of the number, disregarding any factors that are multiples of the square root. It then iterates through the numbers from 2 to the square root of the input number, checking for divisibility. If the number is divisible by any of these factors, it returns `False`, indicating that the number is not prime. If it is not divisible by any of them, it returns `True`, indicating that the number is prime. 

The second function, `prime_length(string)`, takes a string as input and uses `is_prime()` to determine whether the length of the string is a prime number or not. The function first checks if the input is a string and then proceeds to check the length thereof for primality. 

By using `is_prime()` method, the code creates a reusable and efficient solution that minimizes unnecessary checks for factors. 

This solution passes all the test cases provided in the prompt and provides an accurate determination of whether the length of a given string is a prime number or not. 
```python
```

You can test this function directly in the Python interpreter by calling `prime_length()` with different strings.