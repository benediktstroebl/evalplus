Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra "db" characters at the beginning and end of the string:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]  # getting the binary representation without '0b'
    return "db" + bin_str + "db"

# Test cases
decimal_numbers = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, result in zip(decimal_numbers, expected_results):
    assert decimal_to_binary(dec) == result
```
In this code block, the `decimal_to_binary` function takes a decimal number as input and uses the `bin` function to convert it to a binary representation. The `[2:]` slice is used to remove the '0b' part of the binary string. Then, it adds the "db" characters at the beginning and end of the string and returns the modified string.

The script includes test cases that check the function's output against the expected results for two different decimal numbers. The `zip` function is used to iterate over the decimal numbers and expected results simultaneously. Lastly, the `assert` statement checks if the converted binary strings are equal to the expected binary results for each test case.