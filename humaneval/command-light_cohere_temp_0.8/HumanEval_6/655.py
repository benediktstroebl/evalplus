```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces and returns the deepest level of nesting of parentheses.
    Example a implementation uses a last nested level, i. if the nested parentheses are a string is passed in, this function will return an array containing the deepest level of each nesting.
    """
    strings with fewer nested parentheses than the input string will not match.

    Test cases:
    - Test with input "((()))". Should return [2]
    - Test with input "((()()))". Should return [2]
    - Test with input "(() ())". Should return [2]
    - Test with input "()() () ()". Should return [3]
    - Test with input "() (())". Should return []
    - Test with input "((x))". Should return []
    - Test with input "()()".
    """
    stack = []
    for group in s:
        if group == '(':
            stack.append(len)
        else:
            stack.append(group)
    if len(stack) == 0:
                break
    return stack[::-1]
```