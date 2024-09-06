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
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if hex_digits.index(digit) in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count

# Test Suite
def test_hex_key():
    """
    Unit tests for the hex_key function.
    """
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
    assert hex_key("") == 0

test_hex_key()
```

The function `hex_key` works by first setting up a list of hexadecimal digits: `hex_digits = "0123456789ABCDEF"`, then iterating through each digit in the input number, and counting the prime digits among them. Finally, the function returns the count of prime digits. 

The test suite `test_hex_key` verifies the functionality of the `hex_key` function using different test cases. You can add more tests to this test suite to further validate the function's behavior.