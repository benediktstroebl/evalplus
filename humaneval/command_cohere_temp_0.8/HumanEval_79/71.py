Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    binary_string = "{0:b}".format(decimal)
    db_suffix = "db"
    return db_prefix + binary_string + db_suffix

# Test Cases
decimal = 15
expected_result = "db1111db"
result = decimal_to_binary(decimal)
print(f"Test Case:decimal_to_binary({decimal}) == {expected_result}: {result == expected_result}")

decimal = 32
expected_result = "db100000db"
result = decimal_to_binary(decimal)
print(f"Test Case:decimal_to_binary({decimal}) == {expected_result}: {result == expected_result}")

decimal = -1
expected_result = "db111db"
result = decimal_to_binary(decimal)
print(f"Test Case:decimal_to_binary({decimal}) == {expected_result}: {result == expected_result}")

decimal = 0
expected_result = "db0db"
result = decimal_to_binary(decimal)
print(f"Test Case:decimal_to_binary({decimal}) == {expected_result}: {result == expected_result}")

```
This code snippet includes a function called `decimal_to_binary`, which takes a decimal number as input and returns a string that represents the binary equivalent of that number. The function encapsulates the decimal number in the "db" prefix and suffix to ensure the correct binary format.

Moreover, this code includes explicit tests that validate the behavior of the `decimal_to_binary` function. These tests check the function's output against the expected results for a variety of decimal inputs. The function is invoked using different decimal values, and the results are contrasted with the anticipated "db" prefixed and suffixed binary strings.

The test case assertions make it easier to verify the accuracy of the function's output and ensure it complies with the specified requirement of translating decimal numbers to binary format. You can use them to confirm that the function behaves as expected across various scenarios.