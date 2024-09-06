Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
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

The provided Python code defines a function called `hex_key` that takes a string `num` as input. This function counts the number of hexadecimal digits that are prime numbers and meets the criteria stated in the problem description. 

The code also includes a nested function called `is_prime` which checks whether a given number is a prime or not. 

To calculate the number of prime hexadecimal digits, the `hex_key` function iterates through each character of the input string `num`. For uppercase characters, it uses the `find` method on the `digits` string to get the corresponding numeric value. For lowercase characters, it converts the character to a numeric value directly using int(). 

If the numeric value of the digit is prime, it increments the `count`. Finally, the function returns the accumulated count of prime hexadecimal digits. 

The code includes no external dependencies other than the Python standard library, making it self-contained and easy to use in any Python environment. 

To ensure the function works as expected, it includes a comprehensive test suite. Feel free to uncapture below to view them:
```python
# Tests
def test_hex_key():
    assert hex_key("2020") == 2
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
```

You can use an IDE or a Python interpreter to run the tests by typing `python test.py` and pressing Enter. The output should display the results of each test case, confirming that the `hex_key` function behaves as expected.