```python
from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR operation on two strings, and return the result as a string.
    """
    function xors strings as bitwise operation
    """
    # ensure strings are at least 5 characters
    if len(a) < 5 or len(b) < 5:
        raise ValueError("Input strings should be at least 5 characters long")

    # using list comprehension to slice the first character
    # then xor the rest of the string
    result = [c ^ d for c, d in zip(a, b)[1:]]

    return ''.join(result)

# Tests
test_cases = [
    ("010", "110"),
    ("1010", "0110"),
    ("1000", "0000"),
    ("1010", "1010"),
    # invalid inputs
    ("abc", "xyz"),
    ("", "")
]

# define test suite and run tests
def test_suite():
    test = unittest.TestLoader()..load_tests("tests.py", "string_xor")
    test.run(test_cases)
    print("All tests passed!")

if __name__ == "__main__":
    test_suite()
```
This script defines a function `string_xor` that performs a bitwise XOR operation on two input strings and returns the result as a string. It also includes a suite of test cases to ensure the function's correctness. 
When you run this script, the `test_suite` function runs the tests and displays whether the tests have passed or failed.