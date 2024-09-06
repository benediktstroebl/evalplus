```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with nested parentheses and returns the levels of nesting for each group.

    Example: >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for match in re.match.sub(r'\(r"\(\([\])?\s+([\])\))?"mate must match a group of parentheses.
    stack: = []
    for match in re.match.sub().match('\s+match(\([\])?\s+([\])\))', end=''):
        stack.append(match.group(0))
   result.append(len(stack))
        stack = []
    return result
```