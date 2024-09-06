Here is a Python script that includes a self-contained function `separate_paren_groups`, which solves the problem of separating and balancing parentheses in a given string. 

```python
import typing


def separate_paren_groups(parentheses: typing.string.str) -> List[ string containing many groups of nested parentheses.

def test_separate_paren_groups():
    # Test cases for the separate_paren_groups function
    test_cases = [
        ("() () ()")
        ("(()((()))))"),
        ("((((())))())"),
        ("( )( ) ")
    ]

    for test_case in test_cases:
        actual_result = separate_paren_groups(test_case)
        expected_result = ["()", "(())", "(()())"]
        assert actual_result == expected_result


test_separate_paren_groups()
```
This script defines a function `separate_paren_groups` that takes a string containing multiple groups of nested parentheses and returns a list of separate strings with balanced parentheses. 

The `test_separate_paren_groups` function contains several test cases to verify the functionality of the `separate_paren_groups` function. 

The test cases cover various scenarios, including different numbers of nested parentheses and different types of input strings.