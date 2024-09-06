```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function returns a list of deepest level of parentheses in the string s.
    >>> | Score: Each element in the list represents a score, with 0 being the least nesting.
    """
    specific scoring rules:
    - 0: No parentheses found.
    - 1: Open parenthesis only.
    - 2: Close parenthesis only.
    - 3: Both open and close parenthesis.
    - 4: Any nested combination.
    """
    input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For example: Input "(()()) ((())) () ((())()())".
    Return: [2, 3, 1, 3]
    """
    stack: List[int] = []
    n: int = len(s)
    for i in range(n):
        if s[i] == '(':
            stack.append(1)
        else:
            if stack:
                top, score = stack.pop()
                stack.append(4)
                else:
                    stack.append(0)
            stack.append(2)
        stack.append(0)
        stack.append(3)
    return stack
```