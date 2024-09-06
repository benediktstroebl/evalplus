```python
import re

def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    return sum(1 for digit in num if digit in primes and int(digit, 16) <= 36)
```

The function `hex_key` uses a list of prime numbers to iterate through each digit of the input number and determine if it is a prime hexadecimal digit. The sum function is used to count the number of prime digits. 

This solution assumes that the input test cases will be correct and will not throw any `ValueError` when converting hexadecimal digits to decimal values. If you would like to have a more robust solution towards potential incorrect inputs or invalid hexadecimal digits, please specify them in the input so I can adjust the solution accordingly. 

The following test suite is included to ensure that the function behaves as expected:
```python
# Test Suite
num = "AB"
assert hex_key(num) == 1

num = "1077E"
assert hex_key(num) == 2

num = "ABED1A33"
assert hex_key(num) == 4

num = "123456789ABCDEF0"
assert hex_key(num) == 6

num = "2020"
assert hex_key(num) == 2
```