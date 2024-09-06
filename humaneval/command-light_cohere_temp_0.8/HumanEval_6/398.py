Here's the code to solve the problem:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function parses a string of nested parentheses.
    Returns the right deepest level of nesting of parentheses in the string.
    """
    following regular expression:
    <start> .*.* <end>
    """
    start = "("
    end = ")"
    stack = []
    inParen = False

    for char in s:
        if char == start:
            if inPparen:
                stack.append(len)
                inParent = True
        elif char == end:
            if not inPparen:
                inParent = False
                stack.append(0)
            else:
                stack[-1] += 1
        else:
            inParent = False
            stack[-1] += 1

    return stack
```