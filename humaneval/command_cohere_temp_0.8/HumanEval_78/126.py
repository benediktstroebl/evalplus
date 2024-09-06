Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.
    """
    digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = digits.find(char)
        else:
            digit = int(char)
        
        if is_prime(digit):
            count += 1
    return count
```

The provided code defines a Python function called `hex_key` that takes a single argument, `num`, which is a string representing a hexadecimal number. This function's purpose is to count the number of hexadecimal digits that are prime numbers and return this count. To accomplish this, it employs two helper functions: `is_prime`, which checks if a given number is prime, and iterates through each character in the input hexadecimal number. It determines whether each character represents a digit or an uppercase letter. If it's a digit, it converts it to an integer; if it's an uppercase letter, it uses the `find` method to convert it to a digit and then checks if it's a prime digit. The total count of prime digits is returned as the result of this function. 

The `is_prime` function is a standard primality-checking function that iterates through numbers from 2 up to the square root of the given number (a commonly used optimization) and returns `True` if the number is prime and `False` otherwise. 

The code appears to accurately solve the problem statement and is well-structured, employing a modular approach with helper functions. Additionally, the `hex_key` function provides an informative docstring that explains its purpose and behavior, making the code more understandable and maintainable.

This code can be run as a Python script and tested as needed for specific inputs.  For example:
```python
# Test the solution
assert hex_key("AB") == 1
assert hex_key("1077E") == 2
assert hex_key("ABED1A33") == 4
assert hex_key("123456789ABCDEF0") == 6
assert hex_key("2020") == 2
``` 
The code and tests are also structured to be easily accessible and modifiable, allowing for easy adaptation to address any changes in the problem statement or to improve the solution's efficiency or accuracy, if needed.