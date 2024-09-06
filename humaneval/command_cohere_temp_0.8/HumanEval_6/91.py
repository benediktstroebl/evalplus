```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        level = 0
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The `parse_nested_parens` function iterates through a string containing multiple groups of parentheses separated by spaces. For each group, it uses a stack to keep track of opening parentheses encountered. It increases the `level` whenever an opening paren is added to the stack and decreases it whenever a closing paren is popped from the stack. The function appends the `level` for each group to the `result` list and returns the final list.

This solution has a time complexity of `O(n)` where `n` is the length of the input string, as it performs a single pass to split and process the string.