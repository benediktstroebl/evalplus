Here's a Python script with a self-contained function that solves the problem using a concise and optimized approach:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(parens_level(group)) for group in s.split(' ')]

def parens_level(s: str) -> int:
    if not s:
        return 0
    return 1 + max(parens_level(part) for part in s.split(')'))
```

This script provides the `parse_nested_parens` function, which takes a string input separated by spaces, and maps each string to the deepest level of nesting of parentheses within those strings.

The `parens_level` helper function recursively checks the provided string `s` for nested parentheses, returning the deepest level of nesting. The overall time complexity of this solution is O(N*M) where N is the total length of all strings and M is the maximum depth of any single string. This is much more efficient than the linear approach for each string.