```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        count = 0
        curr = 0
        for char in bracket_str:
            if char == '(':
                count += 1
            else:
                count -= 1
            curr = max(curr, count)
        result.append(curr)
    return result
```
The `parse_nested_parens` function takes a string as input and returns a list of the deepest nesting level of parentheses in each sub-string separated by spaces. It uses a simple loop to keep track of the nesting level of parentheses for each substring.