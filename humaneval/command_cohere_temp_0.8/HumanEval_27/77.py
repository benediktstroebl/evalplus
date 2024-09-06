```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, uses the `swapcase()` method to flip the case. Non-alphabetic characters are left unchanged.

To test this function, you can call it with different input strings and compare the output with the expected results. Here's an example:
```python
# Test case with lowercase and uppercase letters
input_string = 'hello, World!'
expected_output = 'hELLO, wORLD!'
actual_output = flip_case(input_string)

if actual_output == expected_output:
    print("Test passed!")
else:
    print("Test failed! Actual:", actual_output, "Expected:", expected_output)
```

The test case above would pass, and all other test cases should also pass with the provided function. Feel free to modify the test cases to ensure that the function behaves as expected across different scenarios. Let me know if you need further assistance or have additional questions related to the problem!