```python
import re

PRIMES = [2, 3, 5, 7, 11, 13, 17]

def hex_key(num):
    prime_count = sum(digit in PRIMES for digit in re.findall('{:X}', num))
    return prime_count
```

The function `hex_key` takes a hexadecimal number as input and uses a regular expression to find all hexadecimal digits within the number. It then checks each digit against the list of prime numbers to determine if it is a prime. The sum function is used to count the number of prime digits, and the result is returned.

Here is a test suite to ensure the function behaves correctly:
```python
def test_hex_key():
    # Example 1: num = "AB" => 1
    assert hex_key("AB") == 1

    # Example 2: num = "1077E" => 2
    assert hex_key("1077E") == 2

    # Example 3: num = "ABED1A33" => 4
    assert hex_key("ABED1A33") == 4

    # Example 4: num = "123456789ABCDEF0" => 6
    assert hex_key("123456789ABCDEF0") == 6

    # Example 5: num = "2020" => 2
    assert hex_key("2020") == 2

    # Additional test cases
    assert hex_key("22") == 1
    assert hex_key("22AA") == 2
    assert hex_key("A3") == 1
    assert hex_key("B5") == 1
    assert hex_key("C7") == 1
    assert hex_key("D11") == 1
    assert hex_key("E13") == 1
    assert hex_key("F17") == 1
    assert hex_key("1011") == 2
    assert hex_key("1013") == 2
    assert hex_key("1017") == 2
    assert hex_key("101A") == 2
    assert hex_key("101D") == 2
    assert hex_key("1021") == 2
    assert hex_key("1023") == 2
    assert hex_key("1027") == 2
    assert hex_key("1029") == 2
    assert hex_key("1121") == 2
    assert hex_key("1122") == 1
    assert hex_key("1125") == 2
    assert hex_key("1126") == 1
    assert hex_key("1131") == 2
    assert hex_key("1132") == 1
    assert hex_key("1139") == 2
    assert hex_key("1141") == 2
    assert hex_key("1142") == 1
    assert hex_key("1149") == 2
    assert hex_key("1151") == 2
    assert hex_key("1152") == 1
    assert hex_key("1163") == 2
    assert hex_key("1164") == 1
    assert hex_key("1169") == 2
    assert hex_key("1171") == 2
    assert hex_key("1172") == 1
    assert hex_key("1177") == 2
    assert hex_key("1178") == 1
    assert hex_key("1183") == 2
    assert hex_key("1184") == 1
    assert hex_key("1189") == 2
    assert hex_key("1191") == 2
    assert hex_key("1192") == 1
    assert hex_key("1199") == 2
    assert hex_key("11A1") == 2