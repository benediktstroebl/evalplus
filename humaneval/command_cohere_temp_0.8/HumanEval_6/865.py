```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in s.split():
        level = 0
        i = 0
        for char in bracket_level:
            if char == '(':
                i += 1
            elif char == ')':
                i -= 1
            if i < 0:
                break
            level = max(level, i)
        result.append(level)
    return result
```

The specified Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each of the groups separated by spaces.

The function iterates through each bracket level (split by spaces) and maintains a level counter which keeps track of the deepest level of nesting. It uses a counter `i` to keep track of open parentheses '(' encountered, and decrements `i` for each encountered closing parenthesis ')'. The maximum value of `i` across a bracket level provides the deepest level of nesting for that level. This process is encapsulated within a loop that iterates through each character in the bracket level.

The script passes the provided test case as the function successfully returns the correct deepest levels of nesting for the input string.

This solution has appropriate type annotations for the function signature, indicating the expected input type as a string and the return type as a list of integer depths.