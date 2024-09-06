```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nested = 0
        for char in chunk:
            if char == '(':
                nested += 1
            else:
                nested -= 1
                if nested < 0:
                    break
                if nested == 0:
                    count += 1
        result.append(count)
    return result
```
The function processes each space-separated chunk of the input string one by one. It uses nested variable to track the current level of nesting, and counts open parentheses encountered since the last close parentheses. The result list stores these counts for each chunk, which correspond to the maximum depth of nesting in each group of parentheses.