```python
import re

def hex_key(num):
    """
    Receive a hexadecimal number as a string and count the number of hexadecimal digits that are primes.
    """
    # convert string to list of digits
    num = list(num)
    # remove all non hexadecimal digits and convert to integer
    prime_digits = sum(int(d) for d in re.findall(r'[2-9A-DF]', num))
    return prime_digits
```

This script leverages the `re` module to identify all digits that are primes within a hexadecimal number,
and then sums them to return the count.  While the original prompt implied the use of a regEx module, 
the use of `re.findall()` is not explicitly mentioned. The prompt also mentions the need to convert 
the string to an integer, which is a confusing step, as it's not necessary or useful in this context.

Here is a test suite to ensure the function behaves correctly:
```python
def test_hex_key():
    # rudimentary test cases, should all be true
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2

    # edge cases
    assert hex_key("") == 0
    assert hex_key("ABC") == 0
    assert hex_key("XYZ") == 0
    assert hex_key("1") == 0
    assert hex_key("Graham") == 0

test_hex_key()
```

This test suite contains multiple asserts against minimal, edge, and invalid cases, 
and it would be beneficial to include them in the development of your code as well. 
Feel free to customize them to your needs.