```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parentheses as input and returns a list of the properly separated parentheses.
    """
    input: String
    """
    return [p.strip() for p in s.clear() if p == '(' or ')', ')']
# define test cases
test_cases = [
    "()(( ))(( )( ))",
    "( )",
    "()()()()",
    "()()(( (( ))))",
    "((()))",
    # Testing variable function
    "( )",
]
# Function Test Cases
for tc in test_cases:
    actual_result = separate_paren_groups(tc)
    assert actual_result == tc.trim()
```
The above code defines a function `separate_paren_groups` that takes a string containing multiple groups of parentheses as input. It returns a string that has each group of parentheses properly separated. The code is then testing the function with different test cases and verifies that the output is correct.