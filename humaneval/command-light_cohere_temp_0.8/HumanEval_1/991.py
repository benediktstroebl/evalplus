```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of separate and balanced parentheses.
    Return list of balanced parentheses.
    """ Test case for:
        Input: ['(())', '(()())', '()', '()']
        Output: ['((())'),(()()),()', ('()')']
    """
    return [p for p in input_string.replace(')'.replace('()', ''), ',' + '()')
```