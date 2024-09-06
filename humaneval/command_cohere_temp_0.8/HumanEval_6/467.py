```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in string.splitlines(s):
        level = 0
        for char in bracket_level:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        result.append(level)
    return result
```

The code uses a basic iterative approach to parse each line (group of parentheses) and maintain a `level` variable that denotes the current nesting level. Increasing the `level` when encountering `(`, and decreasing it when encountering `)`. The final `level` is then appended to the `result` list.

To run the code successfully, ensure you have the required dependencies, if not, you can run `pip install typing`. The code takes a string input where different groups of parentheses are separated by spaces, and it returns a list where each element represents the deepest nesting level of parentheses in each group.