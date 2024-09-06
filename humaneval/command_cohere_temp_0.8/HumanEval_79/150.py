Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra "db" characters as specified in the problem:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # getting the binary representation without '0b'
    return "db" + bin_str + "db"

# Test Cases
decimal_numbers = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, result in zip(decimal_numbers, expected_results):
    assert decimal_to_binary(dec) == result
```
In this script, the `decimal_to_binary` function takes a decimal number as input. The conversion to binary is done using the `bin` function, which returns a string representation of the binary number. The expression `bin(decimal)[2:]` extracts the actual binary string, skipping the initial '0b'. Finally, the result is returned with the specified "db" characters at the beginning and end.

The test cases at the end ensure that the function produces the expected binary results for the given input decimal numbers.