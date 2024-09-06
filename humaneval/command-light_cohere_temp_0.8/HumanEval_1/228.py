Here is a Python script with a self-contained function that solves the problem of separating nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Remove all spaces and properly separate the parenthesis groups.
    :param s: str - Input string containing nested parentheses
    :return: List of separated strings
    """
    # strip all spaces
    s = s.replace(' ', '', s) 
    # split the string by each open parenthesis
    return [s.replace(')[1:][::1]]
# Test cases
test_cases = [
    '() (( )) (( )( ))',
    '( )',
    '((()))',
    '( )())'
]

for case in test_cases:
    actual_result = separate_paren_groups(case)
    print(case, '->', actual_result)
```

This script defines a function `separate_paren_groups` that takes a string `s` as input, which should contain multiple groups of nested parentheses. It then removes all spaces from the string and splits it by each open parenthesis. The resulting strings are then separated and returned as a list.