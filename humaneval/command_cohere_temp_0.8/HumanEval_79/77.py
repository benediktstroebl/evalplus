Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. 

```python
def decimal_to_binary(decimal):
    bin_string = bin(decimal)[2:]
    return 'db' + bin_string + 'db'

# Test Cases
decimal_values = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, expected in zip(decimal_values, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected
```

This script defines the `decimal_to_binary` function, taking a decimal number as input and returning the binary representation with '0' and '1' characters, prefaced and followed by 'db'. It then tests this function with two test cases, 15 and 32, and verifies that the function's results are correct. 

Let's break down the code:
- `def decimal_to_binary(decimal):` declares a new function called `decimal_to_binary` that takes a single argument called `decimal`.
- `bin_string = bin(decimal)[2:]` converts the decimal number to a binary string and then removes the '0b' prefix.
- `return 'db' + bin_string + 'db'` prefaces the binary string with 'db' and appends 'db' at the end, as specified in the problem statement.
- The test cases and expected results are defined, and then the function is tested against these test cases. 

This code is an example of how to solve a particular problem in a self-contained manner, as it includes the function and tests in one snippet.