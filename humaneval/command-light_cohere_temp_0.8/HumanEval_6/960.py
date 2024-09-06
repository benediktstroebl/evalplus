```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Function to parse and return the deepest level of nesting for a string of parentheses.
    Args:
        s: str, a string containing multiple groups of parentheses separated by spaces.
    Returns:
    List of position indices of each closed parenthesis in the string.
    """

    string "" returns an empty list [].
    """
    stack: List[int] = []
    result: List[int] = []
    start: int = 0
    for end in range(len(s)):
        if s[end] == '(':
            stack.append(end)
        stack.append(0)
        stack.append(end)
        stack.append(0)
        stack.append(end)
        stack.append(0)
        stack.append(end)
        stack.append(end))
        stack.pop()
        stack.pop()
        stack.append(end) stack.append(0)
        stack.append(end)
        stack.append(end)
        stack.append(end)
        stack.append(end)
        result.append(end - len(stack) - 1)
    return result
```