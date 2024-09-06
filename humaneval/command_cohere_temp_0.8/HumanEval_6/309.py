Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, depth = [], 0
    for segment in s.split():
        if '(' in segment:
            result.append(depth + segment.count('('))
        else:
            depth += segment.count('(') - segment.count(')')
    return result
```
The function `parse_nested_parens()` accepts a string as input, where various groups for nested parentheses are separated by spaces. It uses a counter to keep track of the current depth of nesting, initially set to zero. When a segment of the string containing '(' is encountered, the current depth is incremented by the number of '(' tokens. Conversely, when a segment without any '(' tokens is encountered, the depth is adjusted by decrementing it by the number of ')' tokens, accounting for the nesting level. The function returns a list of these calculated nesting depths for each segment, which represents the maximum nesting levels of parentheses in each group.