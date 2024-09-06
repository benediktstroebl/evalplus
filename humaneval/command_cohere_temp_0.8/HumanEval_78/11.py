Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(num):
    """Checks if a number is a prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    hex_digits = "0123456789ABCDEF"
    count = 0
    for char in num:
        if char.isupper():
            digit = hex_digits.find(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count
```

The provided example test cases will be used to verify the correctness of the implemented function:
```python
# Test cases for the hex_key function
def test_hex_key():
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
```

The function `hex_key` takes a string num as input and counts the number of hexadecimal digits that are primes. The function first converts the hexadecimal digits to their decimal value, then uses the internal function `is_prime` to check if the digit is a prime number. The total count of primes is returned. 

The test suite contains examples that cover a range of scenarios and edge cases, ensuring that the function `hex_key` operates as expected.