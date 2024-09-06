```python
import math

def hex_key(num):
    prime_hex = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    count = 0
    for char in num.upper():
        if char in '0123456789ABCDEF':
            digit = int(char)
            if digit not in prime_hex:
                count += 1
    return count
```

The `prime_hex` list contains prime numbers that are also hexadecimal digits, and the script iterates through each character in the provided string `num`. It determines whether the character is a hexadecimal digit using a character class check, and if so, it converts it to an integer. Subsequently, it checks if the integer is in the `prime_hex` list, which contains only the prime hexadecimal digits. If the digit is not prime, the `count` variable is incremented, and finally, the function returns the count of prime hexadecimal digits.

Here is a simple test suite to ensure the functionality of the code:
```python
def test_hex_key():
    assert hex_key("2020") == 2
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("FG") == 0
```

This test suite includes a variety of inputs to ensure that the function performs as expected based on the problem statement.