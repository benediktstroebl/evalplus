```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        nesting_level = 0
        for char in partition:
            if char == '(':
                nesting_level += 1
            elif char == ')':
                nesting_level -= 1
            level = max(level, nesting_level)
        result.append(level)
    return result
```

The code uses a simple approach to parse the string and determine the maximum nesting level of parentheses in each group. It iterates through each character in a partition (a group of parentheses), increments a `level` variable for every '(' encountered, and decrements it for every ')' encountered. The `level` variable gets updated only if the current nesting level is greater than the previous.

The above approach is efficient because the maximum depth of any particular group of parentheses can be calculated by merely examining the open and closed parentheses and determining the maximum depth of nesting. There is no need for fancy recursive parsing techniques. It is a linear time algorithm.