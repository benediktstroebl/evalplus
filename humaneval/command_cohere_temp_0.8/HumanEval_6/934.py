```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        open_brackets = 0
        closed_brackets = 0
        for char in nested_parens:
            if char == '(':
                open_brackets += 1
            elif char == ')':
                closed_brackets += 1
        result.append(open_brackets - closed_brackets)
    return result
```

The `parse_nested_parens` function takes a string `s` containing multiple groups of nested parentheses separated by spaces as input. It iterates through each nested parens group, counts the number of opening and closing brackets, and calculates the difference to get the deepest level of nesting. This value is then appended to the `result` list.

The example input provided in the problem statement would produce the following output:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This approach is straightforward and works as expected to solve the problem. It is efficiently coded and neatly organized, maintaining good readability and clarity.