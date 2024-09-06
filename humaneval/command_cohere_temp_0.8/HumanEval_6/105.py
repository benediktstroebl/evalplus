```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        count = 0
        nested = 0
        level = 0
        for char in bracket_str:
            if char == '(':
                count += 1
                nested += 1
            else:
                count -= 1
                if not count:
                    level += nested
                    nested = 0
        result.append(level)
    return result
```
The function processes each group of parentheses separately and counts the number of '(' and ')' characters to determine the deepest level of nesting. The output provides the list of deepest nesting levels for each group of parentheses.