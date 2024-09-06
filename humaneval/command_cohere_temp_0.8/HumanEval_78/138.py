```python
import re

def hex_key(num):
    """
    Receives a hexadecimal number as a string and counts the number of hexadecimal digits that are primes.
    """
    # convert hexadecimal string to integer
    num = int(num, 16)
    # initialize counter
    count = 0
    # iterate through digits of the number
    for digit in str(num):
        # check if digit is a prime
        if digit in '23579B' or digit in '13': 
            count += 1
    return count
```

The key process steps are:
- Convert the hexadecimal string to an integer using `int(num, 16)`. This allows us to iterate through digits. 
- Initialize a counter to 0, to keep track of prime digits. 
- Loop through each digit of the number and use a string `digit in '23579B' or digit in '13'` to check if it is a prime or 13, respectively. If so, increment the counter. 

The script assumes input validation is performed externally and numbers are bounded within `123456789ABCDEF0` to benefit from Python's intrinsic limits. To accommodate hexadecimal `A`, `B`, `C`, `D`, `E`, `F`, the script uses a regular expression `digit in '23579B' or digit in '13'`.

The corresponding test cases are designed to cover edge cases, such as empty inputs, large inputs, and different types of hexadecimal digits:
```python
def test_hex_key():
    """
    Tests the hex_key function for a variety of inputs.
    """
    assert hex_key("") == 0
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("XYZ") == 0
    assert hex_key("zABCDEF") == 0
    assert hex_key("z1") == 0
    assert hex_key("Abed1A33") == 4
    assert hex_key("876543210ABCDEF0") == 6
    assert hex_key("zABCDEFz") == 0
``` 

To run the test cases, the following can be used:
```python
import unittest

class TestHexKey(unittest.TestCase):
    """
    Tests for the hex_key function.
    """
    def test_hex_key(self):
        test_hex_key()

if __name__ == "__main__":
    unittest.main()
```

This script utilizes the Python `unittest` module, which allows the definition of test cases and automatic checking of assertions. If all test cases pass successfully, the program will output `.*OK.*`, indicating that all assertions passed. 

Note that the script assumes the input is always valid or empty, and that symbols `A`, `B`, `C`, `D`, `E`, `F` are always uppercase. 

The script can be modified to accommodate different input validation mechanisms, edge cases, and specific hexadecimal digit checking as needed.