Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = ''
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_string = str(remainder) + binary_string
    binary_string = 'db' + binary_string + 'db'
    return binary_string

# Test Cases
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(32) == 'db100000db'
```

This code snippet defines the `decimal_to_binary` function, which takes a decimal number as input and converts it to binary format according to the problem statement. The function uses a `while` loop to iterate through the decimal representation of the number and accumulates the binary representation. It ensures that the resulting string starts and ends with "db" for formatting purposes. The provided test cases check if the function produces the expected binary strings for 15 and 32.