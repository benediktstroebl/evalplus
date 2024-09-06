```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """ Parses a string containing nested parentheses and returns the deepest level of nesting.
    >>> assert parse_nested_parens('(()) ((())) () ((()))()') == [2, 3, 1, 3], "Test failed!"
    >>> parse_nested_parens('(()()) ((())) () ((()))()')')
    [2, 3, 1, 4]
    """
    stack = []
    for c in s:
        if c == '(':
            stack.append(True)
        else:
            stack.pop()
       while stack:
                nesting_level = stack.pop()
               max_ nesting_level = len(stack)
                yield nesting_level

# Test the function
print(parse_nested_parens('(()) ((())) () ((()))()'))
```