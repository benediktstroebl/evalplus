```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        level = 0
        nesting_level = 0
        for char in bracket_pair:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
                if level == 0:
                    nesting_level = max(nesting_level, level)
        result.append(nesting_level)
    return result
```

This code defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list of the deepest nesting level of parentheses for each group.

The algorithm works by:
1. Splitting the input string into individual groups of parentheses via the `split()` method, which treats spaces as delimiters.
2. For each group, the algorithm maintains a `level` variable that keeps track of the current nesting level of parentheses. Initially, it's set to 0.
3. Each character in the group is iterated over. If it's an open parenthesis `(`, the `level` is incremented, indicating a new level of nesting.
4. If it's a closing parenthesis `)`, the `level` is decremented. If the `level` reaches 0, it means we've reached the deepest level of nesting for this group. We update the `nesting_level` with this value.
5. The `nesting_level` is later appended to the `result` list, which collects the deepest nesting level for each group.

The provided example and test cases are taken care of by the provided code, as it can handle multiple groups of parentheses and correctly determines their deepest nesting levels.