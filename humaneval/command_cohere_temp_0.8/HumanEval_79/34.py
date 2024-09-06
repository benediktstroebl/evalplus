Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = ''
    while decimal > 0:
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2
    return 'db' + binary_string + 'db'

# Test cases
decimal_15 = decimal_to_binary(15)
assert decimal_15 == 'db1111db'

decimal_32 = decimal_to_binary(32)
assert decimal_32 == 'db100000db'
```
This script defines the `decimal_to_binary` function, which takes a decimal number as input and converts it to its binary representation. The function uses a while loop until the input number becomes 0. In each iteration, it calculates the remainder of the current number divided by 2, which represents the binary digit at the current position. These digits are accumulated in the `binary_string` and stored with an extra 'db' at the beginning and end as specified in the prompt.