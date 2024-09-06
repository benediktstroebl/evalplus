Here's a Python code block with a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation, with extra '0's and '1's at the start and end to maintain a consistent length:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal))+4, '0')
    return binary

# Test Cases
decimal_numbers = [15, 32, 63, 45]
expected_results = ['db1111db', 'db100000db', 'db111111db', 'db1001101db']

for dec, result in zip(decimal_numbers, expected_results):
    assert decimal_to_binary(dec) == result
```

In this script, the `bin` function converts the decimal number to its binary representation. We then use `replace` to replace the '0b' prefix with 'db' to make the output more readable. Finally, the `rjust` function ensures the binary string is a consistent length by adding '0's to the beginning and end if needed.