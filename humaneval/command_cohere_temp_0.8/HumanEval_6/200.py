```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        level = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
            level = max(level, nest)
        result.append(level)
    return result
```

The code uses a simple approach to parse the string and counts the deepest level of nesting for each group of parentheses. It iterates through each `chunk` which is a part of the string divided by spaces, and each `chunk` is checked to determine the current nesting level `nest` by counting opening parentheses `'('` and subtracting closing parentheses `')'`. The maximum value between the current nesting level and the previous one is used as the maximum nesting level for the given `chunk` and is stored in the `result` list. The given example and tests will be passed by this solution. 

You can test this function by calling it with different input values and comparing the results with the expected output.