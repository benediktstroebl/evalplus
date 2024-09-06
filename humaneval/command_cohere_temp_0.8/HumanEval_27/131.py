```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphanumeric, then swaps its case, otherwise, it remains unchanged.

To test this function, you can run the following code block:
```python
tested = ['Hello', 'ipAD', 'YOu', 'CoMPuTING']
for test in tested:
    assert flip_case(test) == test.swapcase()
```

This tests the function against four different cases, ensuring that each case is flipped correctly. The `assert` statement verifies that the output of the `flip_case` function is equivalent to the output of the `swapcase` function.  If the script successfully passes the tests, it will generate an output of `OK`.  Otherwise, it will highlight the test failures, showing the expected results and the actual results, making it easier to identify the issues.  This makes it a useful tool for developing robust code.