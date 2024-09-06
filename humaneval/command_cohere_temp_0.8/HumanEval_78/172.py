```python
import math

def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in digits and is_prime(int(digit)):
            count += 1
    return count
```

The solution algorithm is the following:
1. The function `hex_key()` takes a hexadecimal number as a string `num` as an input.
2. The function iterates through each digit of the string `num` and checks if the digit is a hexadecimal digit (0-9, A-F).
3. For each digit found in 'digits', it checks if it's a prime number using the `is_prime()` function. 
4. If the digit is both a hexadecimal digit and a prime number, it increments the count.
5. The function returns the total count of prime hexadecimal digits found in the input number.

Note that the `is_prime()` function implements a simple primality test that checks if a number is divisible by any integer between 2 and the square root of the number. If the number is divisible by any of these integers, it returns `False` to the caller, otherwise, it returns `True`. 

Also, you can adapt the solution using the `math` library:
```python
def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

The tests are the following:
```python
def test_hex_key():
    """Test cases for hex_key."""
    assert hex_key("2020") == 2
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("XYZ") == 0
```

You can run the tests with the following command:
```python
test_hex_key()
```

This command will execute the test cases and display the test results, showing if the function `hex_key()` behaves as expected.