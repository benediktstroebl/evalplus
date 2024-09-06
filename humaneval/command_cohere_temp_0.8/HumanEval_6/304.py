```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        nested_level = 0
        for char in nested_parens:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
                nested_level = max(nested_level, current_level)
        result.append(nested_level)
    return result
```

This code defines a function `parse_nested_parens` that takes in a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list of the deepest nesting level of parentheses for each group.

The `result` list is initialized to store the output for each group of parentheses, and the loop splits the input string into separate groups using the `split()` method.

For each group, the loop determines the deepest level of nesting by keeping track of the current nesting level `current_level` whenever a '(' character is encountered, and decrementing it when a ')' character is encountered. The `nested_level` is updated to the maximum value between its current value and the current nesting level.

After processing all characters in a group, the `result` list is appended with the `nested_level` for that group. Finally, the function returns the `result` list containing the deepest nesting level for each group of parentheses.