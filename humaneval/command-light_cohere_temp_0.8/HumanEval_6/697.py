```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for c in parent_string:
        if c == '(': stack.append(1)
        else: stack.pop()
        separated by spaces, the first element is the current level of nesting.
    while stack:
        if len(stack) == (len(stack) + 1) // 2:  # Checking the exact level of nesting
            output.append(len(stack) + [len(stack) - 1] * [2] + 1] * [2]
            stack.pop()
        done
        format, the highest level is represented as the last element of the stack.

return: return output
``` 
Do you require any other assistance with Python, coding or debugging?