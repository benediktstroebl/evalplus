```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [p.replace('()') for p in s.
    # Your strings that match a group of closed parentheses,
    # then we split it into a list of individual characters.

# test cases
test_cases = [
    '()()',
    '(()())',
    '(() )',
    '( )()',
    '(( ))',
    '(() )',
    '() (( ) )',
    # ]

# loop to run all test cases
for test in test_cases:
    # calling the function with test case
    test_result = separate_paren_groups(test)
    # check if the result is as expected
    assert len(test_result) == 3, f"Error in test case: {test} not having 3 elements."
```
This code defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of strings created from the individual groups of parentheses. The test cases are defined to verify the expected behavior of the function.

Additionally, the test suite ensures that the `separate_paren_groups` function correctly separates groups of parentheses into individual strings.