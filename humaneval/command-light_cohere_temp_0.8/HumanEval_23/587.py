Here's the provided Python script with the function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
test_strlen = {}
test_strlen[''] = 0
test_strlen['abc'] = 3

# Main function call
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

In this script, the `strlen` function takes a string as input and returns its length using the built-in `len()` function. The test suite `test_strlen` contains test cases to ensure the correctness of the `strlen` function. The output of the test cases will be the expected results.