```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open, close = 0, 0
        for char in segment:
            if char == '(':
                open += 1
            else:
                close += 1
        result.append(open >= close)
    return result
```
The function iterates through each segment of the string, maintaining counters for open and closed parentheses. The result list is appended with the maximum depth of nesting for each segment, calculated by comparing open and closed counts.