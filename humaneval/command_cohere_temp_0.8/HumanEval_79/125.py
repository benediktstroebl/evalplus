Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)
```
This function takes a decimal number `decimal` as input and uses the `format` function with a binary prefix (`{0:b}`) to directly convert it to a binary string. It then returns the result prepended and appended with the string "db" to ensure the required format with extra characters.

You can test this function with different decimal inputs to verify its behavior:
```python
# Test cases
decimal_values = [15, 32, 63, 255]
expected_results = ['db1111db', 'db100000db', 'db111111db', 'db11111111db']

for dec, expected in zip(decimal_values, expected_results):
    result = decimal_to_binary(dec)
    print(f"Test case: decimal = {dec}, expected = {expected}, actual = {result}")
```
This will output the test cases and the expected results for comparison.