Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)
```
This function takes a decimal number as its input and converts it to its binary representation. It uses the format method of the str class to convert the decimal number to a binary string. The result is then prefixed and suffixed with "db" to ensure the output matches the specified format. 

To test this function, you can run the following code:
```python
test_cases = [
    (15, "db1111db"),
    (32, "db100000db"),
    (45, "db1010011db"),
    (63, "db1111111db")
]

for decimal, expected in test_cases:
    result = decimal_to_binary(decimal)
    assert result == expected
```
This code provides an example usage of the `decimal_to_binary` function with test cases. It verifies that the function's output is correct for each test case given, ensuring that the function provides the expected binary representation with "db" pads for proper formatting.