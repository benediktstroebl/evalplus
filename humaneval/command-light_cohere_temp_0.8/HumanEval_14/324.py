```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + string.test_cases()

def test_cases():
    # Sample input strings
    strings = [
        "",
        "abc",
        "abc123",
        " Hello, world!",
        "#!/bin defec"
    ]

    # Expected output
    expected = [
        '',
        'a',
        'ab',
        'abc',
        'He ll o w n !',
        '#!/bbROC'
    ]

    # Test function
    for string, expected_out in zip(strings, expected):
        actual_out = all_prefixes(string)
        assert actual_out == expected_out, f"TestCase: {string} actual: {actual_out}, expected: {expected_out}"

# Example:
print(test_cases())
``` 
The function `all_prefixes()` returns a list of all prefixes from shortest to longest of the input string. 

The `test_cases()` function provides sample input strings and the expected output for each test.  The script then runs the test cases and verifies the expected output against the actual output of the `all_prefixes()` function.